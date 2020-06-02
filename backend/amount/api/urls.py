from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from amount.api.views import AmountViewSet
from amount.api import views

router = DefaultRouter()

router.register(r'', views.AmountViewSet, basename='amount')

urlpatterns = [
    path('', include(router.urls)),
]
