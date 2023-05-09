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


def waitPage(request):
    return render(request, "waitPage.html")


def logout(request):
    return redirect('index')



