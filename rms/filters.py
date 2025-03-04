from django_filters import rest_framework as filter
from .models import Food

class FoodFilter(filter.FilterSet):
   class Meta:
      model = Food
      fields = {
         'category':['exact'],
         'price':['gt','lt']
      }