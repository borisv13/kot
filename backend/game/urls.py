from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    url(r'^',views.FrontendAppView.as_view()),
]