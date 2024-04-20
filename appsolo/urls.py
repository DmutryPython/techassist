from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('personal', views.index),
    path('internet_quas', views.inet),
    path('mobile_inet', views.mobile_inet),
    path('television', views.telev)
]
