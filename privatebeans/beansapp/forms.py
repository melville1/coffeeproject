from django.forms import ModelForm
from beansapp.models import  Order





class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']









