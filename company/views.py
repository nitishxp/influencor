# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import CompanyDetails
from grade.settings import BASE_DIR
from django.http import HttpResponse


# Create your views here.
def save_company_details(request):

    if request.method == "POST":
        company_dic = {}
        for c in request.POST.keys():
            if c == "company_presentation":
                continue
            if c == "logo":
                continue
            if c == "csrfmiddlewaretoken":
                continue
            company_dic[c] = request.POST[c]

        company = CompanyDetails.objects.create(**company_dic)
        # now its time to save the file
        company.company_presentation = process_attachments(
            request.FILES['company_presentation'])
        company.logo = process_attachments(request.FILES['logo'])

        return HttpResponse('sads')

    return render(request, 'company.html')


def process_attachments(f):
    import os
    import uuid

    # creation of folder
    temp_dir = '/static/company/'
    dir_path = BASE_DIR + temp_dir

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    f_name = str(uuid.uuid4()) + f.name
    file_path = dir_path + f_name
    destination = open(file_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return temp_dir + f_name
