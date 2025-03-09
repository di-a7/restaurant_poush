from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender = Order)
def on_order_created(sender,instance,**kwargs):
   print("Order signal was triggered.")
   send_mail(
      subject="Order",
      message="Your order has been placed successfully.",
      from_email='diya@gmail.com',
      recipient_list=("a@gmailcom",)
   )