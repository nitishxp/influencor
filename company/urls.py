from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', save_company_details, name="company__save_company_details"),
    url(r'^redirect/(?P<url>[0-9A-z]+)/$',
        redirect_to_company_page,
        name="company__redirect_to_company_page"),
]
