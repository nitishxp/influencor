from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', index, name="investor__index"),
    url(r'^influencor/', influencor, name="influencor"),
]
