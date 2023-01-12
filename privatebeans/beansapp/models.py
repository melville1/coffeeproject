from django.db import models

# Create your models here.
class Tag(models.Model):
    type = models.CharField(max_length=30)
    
    
      

# addressee indicates the recipient of the order not necessarily the person placing the order.
class Addressee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()

    
    def __str__(self):
            return self.name


class Product(models.Model):
    types = models.ManyToManyField(Tag)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField() # different from quantity because price will have decimal because of the cents.
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),)
    addressee = models.ForeignKey(Addressee,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='pending')
    quantity = models.IntegerField(null=True)
    
#a single order only represents one product, several orders can exist with the same product, meaning that i can orders 1-3 
# contain the same coffee type. all these orders have to be associated to one addreesee


