"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('trip/', include('trip.api.urls')),
    url('location/', include('trip.api.urls')),
    url('driver/', include('driver.api.urls')),
    url('NGO/', include('status.api.urls')),
    url('register/', include('status.register.urls')),
    url('login/', include('status.login.urls')), 
    url('amount/', include('amount.api.urls')),
    
    path('', include('payments.api.urls'))
    
    #url(r'^api/paytm/', include('drf_paytm.urls')),
    #path('api/paytm/', include('drf_paytm.urls')),
]
