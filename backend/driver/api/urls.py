from django.urls import path, include
from django.conf.urls import url
from driver.api.views import QRDetail

urlpatterns = [
    url(r'^(?P<qr_string>.+)/$', QRDetail.as_view()),
]

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from driver.api.views import DriverViewSet
from driver.api import views

router = DefaultRouter()

router.register(r'', views.DriverViewSet, basename='driver')
#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
"""