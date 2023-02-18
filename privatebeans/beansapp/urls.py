from django.urls import path
from beansapp.views import HomeView,OrderView,ConfirmationView,ReceiptView,ProductView,EditView,HistoryOrderView,RegistrationView,LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order/' , OrderView.as_view(), name='order' ),
    path('confirmation/<int:id>', ConfirmationView.as_view(), name='confirmation' ),
    path('editorder/<int:id>', EditView.as_view(), name='editorder' ),
    path('receipt/<int:id>', ReceiptView.as_view(), name='receipt' ),
    path('product', ProductView.as_view(), name= 'menu'),
    path('orderhistory/<int:id>', HistoryOrderView.as_view(), name='orderhistory' ),
    path('registration', RegistrationView.as_view(), name= 'registration'),
    path('login', LoginView.as_view(), name= 'login'),

]