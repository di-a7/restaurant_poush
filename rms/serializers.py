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

class OrderItemSerializer(serializers.ModelSerializer):
   food_id = serializers.PrimaryKeyRelatedField(
      queryset = Food.objects.all(),
      source = 'food'
   )
   food = serializers.StringRelatedField()
   class Meta:
      model = OrderItem
      fields = ("food_id","food",)

class OrderSerializer(serializers.ModelSerializer):
   user = serializers.HiddenField(default = serializers.CurrentUserDefault())
   items = OrderItemSerializer(many=True)
   status = serializers.CharField(read_only = True)
   payment = serializers.CharField(read_only = True)
   class Meta:
      model = Order
      fields= ("user","table","status","payment","items")
   
   def create(self, validated_data):
      items_data = validated_data.pop('items')
      order = Order.objects.create(**validated_data)
      
      for item in items_data:
         OrderItem.objects.create(order = order, food = item['food'])
      return order
   
   def update(self, instance, validated_data):
      return super().update(instance, validated_data)