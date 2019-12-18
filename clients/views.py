from django.shortcuts import render
from django.http import HttpResponse

# from django.core.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from clients.forms import KlientForm


def add_model(request):

    if request.method == "POST":
        form = KlientForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = KlientForm()

        return render(request, "my_template.html", {'form': form})


def index(request):
    return HttpResponse("Client app")
