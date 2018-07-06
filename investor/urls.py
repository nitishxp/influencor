from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', index, name="investor__index"),
    url(r'^influencor/', influencor, name="influencor"),
    url(r'^link_company/(?P<pk>[0-9]+)/$', link_company, name="investor__link_company"),
]
