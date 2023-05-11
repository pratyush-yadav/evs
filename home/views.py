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

