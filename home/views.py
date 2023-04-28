from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def vote(request):
    return render(request, "vote.html")


def login(request):
    voterId = request.POST.get("voterId", False)
    print("voterId: ", voterId)
    return HttpResponse("voterId: " + voterId)

