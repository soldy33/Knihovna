from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tabulka', views.KnihovnaViewSet, basename='knihovnaviewset')

urlpatterns = [
    path('', include(router.urls))
]