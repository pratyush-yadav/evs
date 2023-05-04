from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('vote', views.vote, name='vote'),
    path("send_otp", views.send_otp, name="send_otp"),
    path("check_otp", views.check_otp, name="check_otp"),
    path("waitPage", views.waitPage, name="waitPage"),
]
