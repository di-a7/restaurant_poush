from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def destroy(self, request, *args, **kwargs):
      category = self.get_object()
      order_item = OrderItem.objects.filter(food__category = category).count()
      if order_item > 0:
         raise ValidationError({
            "details":"OrderItem has the food of this category. This cannot be deleted"
         })
      category.delete()
      return Response({
         "details":"Category has be deleted."
      },status=status.HTTP_204_NO_CONTENT)

class FoodViewset(viewsets.ModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
