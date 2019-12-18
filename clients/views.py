from django.shortcuts import render
from django.http import HttpResponse

# from django.core.shortcuts import render, redirect
from django import forms
from django.utils import timezone


def index(request):
    return HttpResponse("Client app")
