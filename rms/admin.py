from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display=['name']
   search_fields = ['name']
   list_filter = ['name']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
   list_display = ['name','price','category']
   search_fields = ['name']
   list_filter = ['category']
   list_per_page = 10
   autocomplete_fields = ['category']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
   list_display = ['number','is_occupied']

class OrderItemInline(admin.TabularInline):
   model = OrderItem
   extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   list_display = ['user','table','status','payment',]
   list_filter = ['status']
   search_fields = ['user','table']
   list_per_page = 10
   inlines = [OrderItemInline]
   list_editable = ['status','payment']

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#    list_display = ['food','order']