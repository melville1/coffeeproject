from django.urls import path
from beansapp.views import HomeView,OrderView,ConfirmationView,ReceiptView,ProductView,EditView,HistoryOrderView,RegistrationView
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order/' , OrderView.as_view(), name='order' ),
    path('confirmation/<int:id>', ConfirmationView.as_view(), name='confirmation' ),
    path('editorder/<int:id>', EditView.as_view(), name='editorder' ),
    path('receipt/<int:id>', ReceiptView.as_view(), name='receipt' ),
    path('product', ProductView.as_view(), name= 'menu'),
    path('orderhistory/', HistoryOrderView.as_view(), name='orderhistory' ),
    path('registration/', RegistrationView.as_view(), name= 'registration'),
    # path('login', LoginView.as_view(), name= 'login'),
    # path('accounts/', include('django.contrib.auth.urls'),),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name = 'logout'),
]

