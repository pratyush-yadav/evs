from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def vote(request):
    return render(request, "vote.html")


def login(request):
    voterId = request.POST.get("voterId", False)
    print("voterId: ", voterId)
    return render(request, "otp.html")


def submit_otp(request):
    otp = request.POST.get("otp", False)
    print(otp)
    if otp=="123456":#dummy OTP
        return render(request, "vote.html")
    else:
        return HttpResponse("INCORRECT OTP")
def logout(request):
    return redirect('index')


def waitPage(request):
    return render(request, "waitPage.html")

