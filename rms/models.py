from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# alt + down(select the place to enable cursors)
# ctrl + alt +down
# ctrl + alt +up
# shift + alt + (down/up)
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Food(models.Model):
   name = models.CharField(max_length=50)
   price = models.FloatField()
   category = models.ForeignKey(Category,on_delete=models.CASCADE)
   def __str__(self):
      return f"{self.name} - Rs.{self.price}"

class Table(models.Model):
   number = models.IntegerField()
   is_occupied = models.BooleanField(default=False)

class Order(models.Model):
   COMPLETED = 'C'
   PENDING = 'P'
   IN_PROGRESS = 'IP'

   STATUS_CHOICES = {
      COMPLETED:"Completed",
      PENDING:"Pending",
      IN_PROGRESS:"In Progress"
   }
   
   PAID = 'P'
   UNPAID = 'U'
   
   PAYMENT_CHOICES = {
      PAID : "Paid",
      UNPAID : "Pending"
   }
   user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
   table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
   status = models.CharField(max_length=2,choices=STATUS_CHOICES, default=PENDING)
   payment = models.CharField(max_length=1,choices=PAYMENT_CHOICES, default= UNPAID)


class OrderItem(models.Model):
   food = models.ForeignKey(Food,on_delete=models.PROTECT,related_name='items')
   order = models.ForeignKey(Order,on_delete=models.PROTECT,related_name='items')