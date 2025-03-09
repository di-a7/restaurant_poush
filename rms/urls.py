from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories',CategoryViewset,basename='categories')
router.register(r'foods',FoodViewset,basename='foods')
router.register(r'orders',OrderViewset,basename='orders')

urlpatterns = [
] + router.urls
