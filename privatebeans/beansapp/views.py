from django.shortcuts import render, redirect
from django.views import View
from beansapp.models import Product,Order, Addressee
from .forms import OrderForm
from django.forms import inlineformset_factory


# Create your views here.
class HomeView(View):
    def get (self,request):

        


        
        return render(
        request= request,
        template_name= "home.html",
        context= {}
        )

class OrderView(View):
   
    

    def get (self,request,id):
                                    # The orders will be associated with table Addressee
                                    # second arguments specifies which table it will use to make forms
        OrderFormset = inlineformset_factory(Addressee,Order, fields=['product','quantity'])
        addressee = Addressee.objects.get(id=id) # retrieveing a specific addressee
        formset = OrderFormset(queryset=Order.objects.none(), instance=addressee)

       
        html_data ={ 
            'formset':formset
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )

    def post(self,request,id):
        OrderFormset = inlineformset_factory(Addressee,Order, fields=['product', 'quantity'])
        addressee = Addressee.objects.get(id=id) # retrieveing a specific addressee
        formset = OrderFormset(request.POST, instance=addressee)
        if formset.is_valid():
            formset.save()
        return redirect('confirmation', id)


class EditView(View):

    def get (self,request,id):
        OrderFormset = inlineformset_factory(Addressee,Order, fields=['product','quantity'])
        addressee = Addressee.objects.get(id=1) # retrieveing a specific addressee
        formset = OrderFormset(queryset=Order.objects.none(), instance=addressee)

       
        html_data ={ 
            'formset':formset
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )

       
        
       


       

    def post(self,request,id):
        order= Order.objects.get(id=id)
        order_form= OrderForm(request.POST, instance=order)
        order_form.save()
        return redirect('order', id)

        


   


class ConfirmationView(View):
    def get (self,request,id):
        addressee = Addressee.objects.get(id=id)
        orders = addressee.order_set.all() # give me all the order associated with this customer


        return render(
            request=request,
            template_name='confirmation.html',
            context={
                'addressee':addressee,
                'orders':orders,
            }
        )
    def post(self,request,id):
        if 'edit' in request.POST:
            
            order= Order.objects.get(id=id)
            order_form= OrderForm(request.POST, instance=order)
            order_form.save()
            
            return redirect('order', id)

       

            
        
       



class ReceiptView(View):
    def get (self,request):
        
        
        return render(
        request= request,
        template_name= "receipt.html",
        context= {}
        )



class ProductView(View):
    def get (self,request):
        
        
        return render(
        request= request,
        template_name= "menu.html",
        context= {}
        )