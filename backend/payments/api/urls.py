from django.urls import path, include
from .views import initiate_payment, callback
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from payments.api.views import TransactionViewSet
from payments.api import views

router = DefaultRouter()
router.register(r'', views.TransactionViewSet, basename='transaction')

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('callback/', callback, name='callback'),
    path('transaction-api/', include(router.urls)),
]
