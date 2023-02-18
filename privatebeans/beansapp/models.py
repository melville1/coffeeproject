from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField


# Create your models here.
class Tag(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
            return self.type


    
    
      

# addressee indicates the recipient of the order not necessarily the person placing the order.
class Addressee(AbstractUser):
    
    address = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.IntegerField()
    phone_number = PhoneField(blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    



    
    def __str__(self):
            return self.name


class Product(models.Model):
    types = models.ManyToManyField(Tag)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField() 
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),)
    addressee = models.ForeignKey(Addressee,on_delete=models.SET_NULL,null=True)
   
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='pending')
    
    def get_order_items(self):
        return self.orderitem_set.all()
  

    def get_total(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.product.price * item.quantity
        return total
    
    





class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
    
	

	
