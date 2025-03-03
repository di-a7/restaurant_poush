from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      # fields = ['id','name']
      # exclude  = ['id']
      fields = '__all__'
   
   def save(self, **kwargs):
      validated_data = self.validated_data
      # Category.objects.filter(name = validated_data.get('name'))
      total_number = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
      if total_number > 0:
         raise serializers.ValidationError('Category already exists')
      # category = Category(**validated_data)
      category = self.Meta.model(**validated_data)
      category.save()
      return category
   
class FoodSerializer(serializers.ModelSerializer):
   price_with_tax = serializers.SerializerMethodField()
   category = serializers.StringRelatedField()
   category_id = serializers.PrimaryKeyRelatedField(
      queryset = Category.objects.all(),
      source = 'category'
   )
   class Meta:
      fields = ('id','name',"price","price_with_tax","category_id","category",)
      model = Food
   
   def get_price_with_tax(self, food:Food):
      return food.price * 0.13 + food.price