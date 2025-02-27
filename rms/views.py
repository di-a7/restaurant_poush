from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView, CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
# Create your views here.

class CategoryList(ListAPIView, CreateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView,DestroyAPIView,UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   lookup_field = 'id'
   
   def delete(self,request,id):
      category = Category.objects.get(id = id)
      order_item = OrderItem.objects.filter(food__category = category).count()
      if order_item > 0:
         raise ValidationError({
            "details":"OrderItem has the food of this category. This cannot be deleted"
         })
      category.delete()
      return Response({
         "details":"Category has be deleted."
      },status=status.HTTP_204_NO_CONTENT)
      
      
   # def get(self,request,id):
   #    category = Category.objects.get(id = id)
   #    serializer = CategorySerializer(category)
   #    return Response(serializer.data)
   
   # def put(self,request,id):
   #    category = Category.objects.get(id = id)
   #    serializer = CategorySerializer(category, data = request.data)
   #    serializer.is_valid(raise_exception=True)
   #    serializer.save()
   #    return Response({
   #       "details":"data has been updated."
   #    })
   
   # def delete(self,request,id):
   #    category = Category.objects.get(id = id)
   #    order_item = OrderItem.objects.filter(food__category = category).count()
   #    if order_item > 0:
   #       raise ValidationError({
   #          "details":"OrderItem has the food of this category. This cannot be deleted"
   #       })
   #    category.delete()
   #    return Response({
   #       "details":"Category has be deleted."
   #    },status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','DELETE'])
# def category_detail(request,id):
#    category = Category.objects.get(id = id)
   
#    if request.method == 'GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method == "DELETE":
#       order_item = OrderItem.objects.filter(food__category = category).count()
#       if order_item > 0:
#          raise ValidationError({
#             "details":"OrderItem has the food of this category. This cannot be deleted"
#          })
#       category.delete()
#       return Response({
#          "details":"Category has be deleted."
#       },status=status.HTTP_204_NO_CONTENT)