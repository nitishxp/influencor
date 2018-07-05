# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from grade.settings import BASE_DIR
from django.utils.datastructures import MultiValueDictKeyError
import random
from users.models import UserModel
from itertools import permutations

def index(request):
    return render(request, 'investor.html')