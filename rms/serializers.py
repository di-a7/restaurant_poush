from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      # fields = ['id','name']
      # exclude  = ['id']
      fields = '__all__'

# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only = True)
#    name = serializers.CharField()

#    def create(self, validated_data):
#       return Category.objects.create(**validated_data)
   
#    def update(self, instance, validated_data):
#       instance.name = validated_data.get('name', instance.name)
#       instance.save()
#       return instance