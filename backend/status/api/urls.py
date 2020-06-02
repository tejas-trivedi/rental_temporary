from django.urls import include, path
from django.conf.urls import url
from .views import (NgoList, NgoDetail, NgoNameList)
urlpatterns = [
    url('names/', NgoNameList.as_view()),
    url(r'^$', NgoList.as_view()),
    url(r'^(?P<NGO_id>\d+)/$', NgoDetail.as_view()),
]