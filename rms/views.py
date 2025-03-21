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
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthenticatedOrReadOnly,IsWaiterOrReadOnly
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filter
from .filters import FoodFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
# Create your views here.

class CategoryViewset(viewsets.ReadOnlyModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   # @extend_schema(
   #    parameters=[
   #    OpenApiParameter(name='name', description='Filter by Name', required=False, type=str),
   #    ],
   #    # description='It deletes the category.',
   # )
   def destroy(self, request, *args, **kwargs):
      """
      Can not delete the category listed in OrderItem
      """
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

class FoodViewset(viewsets.ReadOnlyModelViewSet):
   queryset = Food.objects.select_related('category').all()
   serializer_class = FoodSerializer
   pagination_class = PageNumberPagination
   filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
   filterset_class = FoodFilter
   search_fields = ['id','name']
   permission_classes = [IsAuthenticatedOrReadOnly]

class OrderViewset(viewsets.ModelViewSet):
   queryset = Order.objects.prefetch_related('items').all()
   serializer_class = OrderSerializer
   pagination_class = PageNumberPagination
   permission_classes = [IsAuthenticated,IsWaiterOrReadOnly]
