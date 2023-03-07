from django.forms import ModelForm
from beansapp.models import  Order,OrderItem,Addressee,Guest





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
        fields=['first_name','last_name','address','city','state','zipcode','phone_number','username','password','email'] 



class NewUserForm(ModelForm):
    class Meta:
        model= Addressee
        fields=['username','password','email']

class GuestShippingForm(ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"


