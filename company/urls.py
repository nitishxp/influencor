from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', save_company_details, name="company__save_company_details"),
]
