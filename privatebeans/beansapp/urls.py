from django.urls import path
from beansapp.views import HomeView,OrderView,ConfirmationView,ReceiptView,ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order' , OrderView.as_view(), name='order' ),
    path('confirmation', ConfirmationView.as_view(), name='confirmation' ),
    path('receipt', ReceiptView.as_view(), name='receipt' ),
    path('product', ProductView.as_view(), name= 'menu'),

]