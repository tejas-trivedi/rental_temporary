from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from trip.api.views import TripViewSet#, LocationViewSet
from trip.api import views

router = DefaultRouter()

router.register(r't', views.TripViewSet, basename='trip')
#router.register(r'', views.LocationViewSet, basename='location')
#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
