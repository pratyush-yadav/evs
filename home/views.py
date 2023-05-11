from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint

# Create your views here.
def index(request):
    if request.method=="POST" and request.session.get("authentication_status") == "not_logged_in":
        # When voter ID is submitted...
        request.session["authentication_status"] = "voter_id_entered"
        request.session["voter_id"] = request.POST.get("voterId")
        request.session["otp"] = generate_otp(mail_id="dummy-email@gmail.com")
        return render(request, "otp.html")
    
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
            return render(request, "otp.html")
        
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


def vote(request):
    return render(request, "vote.html")


def waitPage(request):
    return render(request, "waitPage.html")


def logout(request):
    request.session["authentication_status"] = "logged_out"
    return redirect('index')


# NON page related functions
def generate_otp():
    otp = randint(100000,999999)
    # code for sending OTP will be added later...
    return str(otp)

