# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import UserModel
from company.models import CompanyDetails

# Create your models here.


class InvestorCompanyLinkModel(models.Model):

    user = models.ForeignKey(UserModel)
    company = models.ForeignKey(CompanyDetails)
    url = models.TextField()


class InvestorCompanyUrlLinkVisitLog(models.Model):

    user = models.ForeignKey(UserModel)
    company = models.ForeignKey(CompanyDetails)
    created_at = models.DateTimeField(auto_now=True)
