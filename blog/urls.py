from django.conf.urls import url
from django.contrib import admin
from .views import(
    blogbs,
    myblog,
    account,
)

urlpatterns = [
    url(r'^$',blogbs),
    url(r'^myblog', myblog),
    url(r'^account', account),
]
