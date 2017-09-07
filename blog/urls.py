from django.conf.urls import url
from django.contrib import admin
from .views import(
    #bloghome,
    #blog88,
    #blogtest,
    #detail,
    #blog44form,
    blogbs,
)

urlpatterns = [

    #url(r'^$', blogbs),
    #url(r'^blog88/$', blog88),
    #url(r'^blogtest/$', blogtest),
    #url(r'^(?P<id>\d+)/$', detail, name="Detail"),
    #url(r'^blog44form', blog44form, name="Form"),

    url(r'^$',blogbs),
    #url(r'^Blog/', "views.bloghome"),
]
