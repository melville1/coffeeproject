from django.forms import ModelForm
from beansapp.models import  Order,OrderItem,Addressee





class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['addressee']

class AddresseeForm(ModelForm):
    class Meta:
        model= Addressee
        fields=['first_name','last_name','address','city','state','zipcode','email','phone_number','date_of_birth','password','username'] 

class RegistrationForm(ModelForm):
    class Meta:
        model= Addressee
        fields=['username','password',]





