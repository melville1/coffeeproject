from django.urls import path
from beansapp.views import HomeView,OrderView,ConfirmationView,ReceiptView,ProductView,EditView,HistoryOrderView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order/<int:id>' , OrderView.as_view(), name='order' ),
    path('confirmation/<int:id>', ConfirmationView.as_view(), name='confirmation' ),
    path('editorder/<int:id>', EditView.as_view(), name='editorder' ),
    path('receipt/<int:id>', ReceiptView.as_view(), name='receipt' ),
    path('product', ProductView.as_view(), name= 'menu'),
    path('orderhistory/<int:id>', HistoryOrderView.as_view(), name='orderhistory' )

]