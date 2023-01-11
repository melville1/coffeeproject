from django.forms import ModelForm
from beansapp.models import ProductsInOrder, Order





# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         # fields = '__all__'






class ProductsInOrderForm(ModelForm):
    class Meta:
        model = ProductsInOrder
        fields = '__all__'


