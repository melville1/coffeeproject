from django.forms import ModelForm
from beansapp.models import  Order,OrderItem





class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']









