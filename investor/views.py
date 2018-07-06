# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.core.urlresolvers import reverse
from grade.settings import BASE_DIR
from django.utils.datastructures import MultiValueDictKeyError
import random
from users.models import UserModel
from itertools import permutations
from company.models import CompanyDetails
from investor.models import InvestorCompanyLinkModel


def index(request):
    return render(request, 'investor.html')


def link_company(request, pk):
    company_obj = CompanyDetails.objects.get(pk=pk)
    investor = InvestorCompanyLinkModel.objects.filter(
        user=request.user, company=company_obj)

    if not investor.exists():
        import uuid
        url = str(uuid.uuid4())
        url = url.replace('-', '')
        investor_company_link_obj = InvestorCompanyLinkModel()
        investor_company_link_obj.user = request.user
        investor_company_link_obj.company = company_obj
        investor_company_link_obj.url = url
        investor_company_link_obj.save()
    else:
        investor = investor.first()
        url = investor.url

    url = request.get_host() + reverse(
        'company__redirect_to_company_page', args=(url, ))
        
    return JsonResponse(url, safe=False)
