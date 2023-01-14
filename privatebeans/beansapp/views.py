from django.shortcuts import render, redirect
from django.views import View
from beansapp.models import Product,Order, Addressee,OrderItem
from .forms import OrderItemForm
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
                                    # The orders will be associated with the Order table
                                    # second arguments specifies which table it will use to make forms
                                    # we are then able to make one form from these 2 tables.
        OrderItemFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
        #inlineformfactory allow you to create multiple forms at once. makes it more efficient.
        # # the form will only only contain attributes that are contain within orderitem table 
        formset = OrderItemFormset() #because line 28  is returning a function we have paranthesis.
       
        html_data ={ 
            'formset':formset
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )

    def post(self,request,id):
        OrderItemFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
        addressee = Addressee.objects.get(id=id) # we are getting the addresse - a set up for the following line
        order = Order.objects.create(addressee=addressee) # order is created connecting it to the addressee
        formset = OrderItemFormset(request.POST, instance=order)
        # we are calling the OrderItemFormset and filling it with the post data and then associating with the 
        # order from line 47 the "instance" in this case means associating with the order
        # what is happening here is that line 45 calls the form because the post needs it, then 
        # we get the adresse id this is the set up for the follwing line (47)because we will then 
        # create an order and associate it with the addressee and his/her info
        #line 48 then passes the data that was created from the addresse which he created in the post and associates 
        # to the order from line 47.
        if formset.is_valid():
            formset.save() # this adds the data to the database that come from the formset
        return redirect('confirmation', order.id ) # this redirects us to confirmation 
        # the second argument "create.id" grabs the id from the order it does because an object was created
        # from line 47, therefore we not only access to the id but any other attribute that object may contain
        # keep in mind this order.id now contains data


class EditView(View):

    def get (self,request,id):
        order = Order.objects.get(id=id)
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'],)
        formset = OrderFormset(instance=order)
    # the order id is already from the previous view here we are accessing and displaying that order 
    # which is why you see it prefilled. 
        html_data ={ 
            'formset':formset
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )

       
    def post(self,request,id):
        order= Order.objects.get(id=id) # this retrieves the order but has the old data 
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'],) # making the formset
        formset = OrderFormset(request.POST, instance=order) 
        #line 87 whatever new data was put in the post whether it remains the same or not gets resent to the form
        # associated with that orderid 
        if formset.is_valid():
            formset.save() # saves it to the database
        return redirect('confirmation', order.id ) # redirects us to the confirmation with the orderid associated with
        

        


   


class ConfirmationView(View):
    def get (self,request,id): # the id is like a book but only contains the title
        order = Order.objects.get(id=id) # we write this again because we need to acceess the book ( in this case order)
        # the order.objects.get will get me the order associated with id
        # this gets the entire object and all the data that it contains
        orderitems = order.orderitem_set.all() # the "_set.all()" is a django method thats allows us
        # to get everything from orderitem in this example.
        order_total = Order.get_order_items(order) 
        order_price = round(Order.get_order_price(order),2)
        item_totals = Order.get_item_totals(order)
        
        return render(
            request=request,
            template_name='confirmation.html',
            context={
                'order':order,
                'items':orderitems,
                'order_total': order_total,
                'order_price': order_price,
                'item_totals': item_totals,
                
                
            }
        )
    def post(self,request,id):
        order = Order.objects.get(id=id)
        
        if 'delete' in request.POST:
            order.delete()
            return redirect('home')
            
            

       

            
class ReceiptView(View):
    def get (self,request,id):
        order = Order.objects.get(id=id) 
        orderitems = order.orderitem_set.all()
        order_total = Order.get_order_items(order) 
        order_price = Order.get_order_price(order)
        item_totals = Order.get_item_totals(order)
        
        html_data={
            'order':order,
            'items':orderitems,
            'order_total': order_total,
            'order_price': order_price,
            'item_totals': item_totals,
            
            }
        
        return render(
        request= request,
        template_name= "receipt.html",
        context= html_data
        )



class ProductView(View):


    def get (self,request):
        
        
        return render(
        request= request,
        template_name= "menu.html",
        context= {}
        )

class HistoryOrderView(View):
    def get (self,request,id):
        addressee = Addressee.objects.get(id=id) 
        addressehistory = addressee.order_set.all()
        

        html_data ={
            'addressee':addressee,
            'addressehistory': addressehistory,

        }

        return render(
        request= request,
        template_name= "orderhistory.html",
        context= html_data
        )
