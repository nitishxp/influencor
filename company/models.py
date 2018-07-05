# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class CompanyDetails(models.Model):
    director_name = models.TextField(null=True)
    director_contact = models.TextField(null=True)
    director_email = models.TextField(null=True)
    company_name = models.TextField(null=True)
    company_registration_number = models.TextField(null=True)
    company_address = models.TextField(null=True)
    company_city = models.TextField(null=True)
    company_presentation = models.TextField(null=True)
    industry = models.TextField(null=True)
    investor_name = models.TextField(null=True)
    incorporation_date = models.TextField(null=True)
    product_description = models.TextField(null=True)
    logo = models.TextField(null=True)
    company_url = models.TextField(null=True)
    bank_name = models.TextField(null=True)
    bank_acc_no = models.TextField(null=True)
    bank_ifsc_code = models.TextField(null=True)
