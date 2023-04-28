from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('vote', views.vote, name='vote'),
    path("login", views.login, name="login"),
]
