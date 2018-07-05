# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.


class UserModel(AbstractUser):

    role = models.TextField(null=True, default='investor')
    name = models.TextField(null=True)
    social_media = models.TextField(null=True)
    physical_shows = models.TextField(null=True)
    stage_show_name = models.TextField(null=True)
    bank_name = models.TextField(null=True)
    bank_acc_no = models.TextField(null=True)
    bank_ifsc_code = models.TextField(null=True)
    social_media_url = models.TextField(null=True)
    no_of_followers = models.TextField(null=True)

    class Meta:
        db_table = 'users'