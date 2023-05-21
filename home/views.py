from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from random import randint
import smtplib
from .models import Voter

# Create your views here.
@never_cache
def index(request):
    if request.method=="POST" and request.session.get("authentication_status") == "not_logged_in":
        # When voter ID is submitted...
        request.session["authentication_status"] = "voter_id_entered"
        voter_id = request.POST.get("voterId")
        request.session["voter_id"] = voter_id
        # check if the voter id is valid and fetch its email id...
        try:
            email = Voter.objects.get(voter_id=voter_id).email
            request.session["otp"] = generate_and_send_otp(recipient=email)
            return render(request, "otp.html", {"email": email[:2]+"**********"+"@"+email.split("@")[-1]})
        except Voter.DoesNotExist:
            request.session["authentication_status"] = "not_logged_in"
            return render(request, "index.html", {"message": "Invalid Voter ID : please enter a valid Voter ID !!!"})
    
    elif request.method=="POST" and request.session.get("authentication_status") in ("voter_id_entered", "login_failed"):
        # When OTP is submitted...
        sent_otp = request.session.get("otp", False)
        entered_otp = request.POST.get("otp", False)
        if entered_otp == sent_otp:
            # User entered corret OTP...
            request.session["authentication_status"] = "logged_in"
            # redirection will be based on the voting status as per user and date/time...
            # will be working on it later...
            return redirect("vote")
        else:
            # User entered incorret OTP...
            request.session["authentication_status"] = "login_failed"
            return render(request, "otp.html", {"message": "Incorrect OTP !!!"})
        
    elif request.session.get("authentication_status")=="logged_out":
        # when user logged out
        request.session["authentication_status"] = "not_logged_in"
        request.session["voter_id"] = None
        request.session["otp"] = None
        return render(request, "index.html", {"message": "User logged out successfully !!!"})
    
    else:
        # when site is normally visited
        request.session["authentication_status"] = "not_logged_in"
        request.session["voter_id"] = None
        request.session["otp"] = None
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


@never_cache
def vote(request):
    if request.session.get("authentication_status")=="logged_in":
        return render(request, "vote.html")
    else:
        return redirect("index")


def waitPage(request):
    return render(request, "waitPage.html")


def logout(request):
    request.session["authentication_status"] = "logged_out"
    return redirect('index')


# NON page related functions
def generate_and_send_otp(recipient):
    otp = randint(100000,999999)
    print(f"@generate_otp: Generated OTP:....................................................     {otp}    <<<<<")
    
    message = f"Subject: OTP for evs\n\n{otp} is your OTP for login to e-Voting System. For security reasons, do not share this OTP with anyone."

    try:
        # read sender's email_id and app_password from file...
        with open("static/mail_credentials.txt") as mail:
            sender, password = mail.read().split("\n")

        # sending otp email...
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
            # context = ssl.create_default_context()
            # server.starttls(context=context)
            server.starttls()
            server.login(sender, password)
            server.sendmail(from_addr=sender, to_addrs=recipient, msg=message)
    
    except FileNotFoundError:
        print("Unable to send OTP : (Login credentials not found !)...")
    
    except Exception as e:
        print("Unable to send OTP : (Cannot connect to internet)...")
    
    return str(otp)

