# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from users.models import UserModel
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def signup(request):
    if request.method == "POST":
        user = {}
        for c in request.POST.keys():
            if c != 'csrfmiddlewaretoken' and c != 'password':
                user[c] = request.POST[c]
        user = UserModel.objects.create(**user)
        user.set_password(request.POST['password'])
        user.save()
    return render(request, 'registration/signup.html')


def index(request):

    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('investor__index'))
            # Redirect to a success page.
        else:
            pass
            # Return an 'invalid login' error message.

    return render(request, 'registration/login.html')
