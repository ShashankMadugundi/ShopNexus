from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
# Create your views here.
from django.contrib import messages
from .models import Product,Customer,Cart,OrderPlaced
from .forms import CustomerRegistrationForm 
from .forms import LoginForm
from .forms import ProfileForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth import logout

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_count=Cart.objects.filter(user=request.user).count()
    else:
        cart_count=0
    return {"cart_count":cart_count}

def home(request):
    latest_products = Product.objects.all().order_by('-id')[:12]
    # if(request.user.is_authenticated):
    women_top=Product.objects.filter(category="Women's Top Wear").order_by('-id')[:12]
    men_top=Product.objects.filter(category="Men's Top Wear").order_by('-id')[:12]
    men_bottom=Product.objects.filter(category="Men's Bottom Wear").order_by('-id')[:12]
    women_bottom=Product.objects.filter(category="Women's Bottom Wear").order_by('-id')[:12]
    mobiles=Product.objects.filter(category="Mobiles").order_by('-id')[:12]
    return render(request,"app/home.html",{
        "products":latest_products,
        "women_top":women_top,
        "men_top":men_top,
        "men_bottom":men_bottom,
        "women_bottom":women_bottom,
        "mobiles":mobiles
    })


def user_login(request):
    if(request.method=="POST"):
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,"app/home.html")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})
                
    # return render(request,"app/login.html")


class register(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"app/register.html",{
            "form":form
        })
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!!! You have successfully Registered')
        return render(request,"app/register.html",{
            "form":form
        })
        
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page or any other page after logout
       
# def login(request):
#     form=
    

def cart(request):
    data=Cart.objects.filter(user__username=request.user.username)
    products=[]
    quantity=[]
    total=0
    discount=0
    price=0
    prod_price=[]
    for i in data:
        prod_price.append(i.quantity*i.product.discount_price)
        quantity.append(i.quantity)
        products.append(i.product)
        total+=(i.quantity)*i.product.discount_price
        price+=(i.quantity)*i.product.selling_price
        discount+=(i.quantity)*(i.product.selling_price-i.product.discount_price)
    cart_items = zip(products, quantity,prod_price)
    return render(request,"app/cart.html",{
        "cart_items": cart_items, 
        "products":products,
        "total":total,
        "discount":discount,
        "price":price,
        "quantity":quantity,
        "prod_price":prod_price
        
    })
    
    
def plus_cart(request):
    if request.method=="GET":
        # print(request.GET['prod_id'])
        prod_id=request.GET['prod_id']
        # print(prod_id)
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        # print(c.product.title)
        # products=[]
        total=0
        discount=0
        price=0

        # for i in c:
        quantity=(c.quantity)
        # total+=(c.quantity)*c.product.discount_price
        # price+=(c.quantity)*c.product.selling_price
        # discount+=(c.quantity)*(c.product.selling_price-c.product.discount_price)
        # print(total)
        # cart_items = zip(products, quantity)
        
        
        
        data=Cart.objects.filter(user__username=request.user.username)
        total=0
        discount=0
        price=0

        for i in data:
            total+=(i.quantity)*i.product.discount_price
            price+=(i.quantity)*i.product.selling_price
            discount+=(i.quantity)*(i.product.selling_price-i.product.discount_price)
        data={
            'quantity':quantity,
            'price':price,
            'total':total,
            'discount':discount
        }
        return JsonResponse(data)
    
    
def minus_cart(request):
    if request.method=="GET":
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        total=0
        discount=0
        price=0
        quantity=(c.quantity)
        data=Cart.objects.filter(user__username=request.user.username)
        total=0
        discount=0
        price=0

        for i in data:
            total+=(i.quantity)*i.product.discount_price
            price+=(i.quantity)*i.product.selling_price
            discount+=(i.quantity)*(i.product.selling_price-i.product.discount_price)
        data={
            'quantity':quantity,
            'price':price,
            'total':total,
            'discount':discount
        }
        return JsonResponse(data)
    
    
    
def remove_cart(request,prod_id):
    if request.method=='POST':
        # print(prod_id)
        Cart.objects.filter(Q(product=prod_id) & Q(user=request.user)).delete()
        return redirect("cart")
class profile(View):
    def get(self,request):
        form=ProfileForm()
        return render(request,"app/profile.html",{
            "profileForm":form,
            "active":"btn-primary"
        })
    def post(self,request):
        form=ProfileForm(request.POST)
        if(form.is_valid()):
            user=request.user
            name=form.cleaned_data.get('name')
            print(name)
            locality=form.cleaned_data.get('locality')
            city=form.cleaned_data.get('city')
            state=form.cleaned_data.get('state')
            zipcode=form.cleaned_data.get('zipcode')
            reg=Customer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Successfully Updated your profile!!!")
            return render(request,"app/profile.html",{
                "profileForm":ProfileForm(),
                
            })
            
    # if(request.method=="POST"):
    #     form=LoginForm(request.POST)
    #     if(form.is_valid()):
    #         name=form.cleaned_data.get('name')
    #         locality=form.cleaned_data.get('locality')
            
        
    # return render(request,"app/profile.html")
def address(request):
    data=Customer.objects.filter(user=request.user)
    # print(data[0].city)
    return render(request,"app/address.html",{
        "fields":data
    })
    
def orders(request):
    orders=OrderPlaced.objects.filter(Q(user=request.user))
    price=[]
    for order in orders:
        price.append(order.product.discount_price*order.quantity)
    result=zip(orders,price)
    return render(request,"app/orders.html",{
        "orders":orders,
        "result":result
    })

def changepassword(request):
    return render(request,"app/changepassword.html")

def checkout(request):
    userData=Customer.objects.filter(user=request.user)
    items=Cart.objects.filter(user=request.user)
    price=[]
    total=0
    # print(items)
    for item in items:
        price.append(item.quantity*(item.product.discount_price))
        total+=(item.quantity*item.product.discount_price)
    goods=zip(items,price)
    return render(request,"app/checkout.html",{
        "items":items,
        "userData":userData,
        "price":price,
        "goods":goods,
        "total":total
    })

def payment(request):
    if(request.GET.get('custid')):
        cust_id=request.GET['custid']
        # print(cust_id)
        customer=Customer.objects.get(id=cust_id)
        cart=Cart.objects.filter(user=request.user)
        for c in cart:
            OrderPlaced(user=request.user,customer=customer,product=c.product,quantity=c.quantity).save()
            c.delete()
        return redirect("/orderplaced")
    else:
        return redirect("/profile")



def productdetail(request,pk,cat):
    if(request.method=='GET'):
        # prod=Product.objects.get(pk=pk)
        if(request.user.is_authenticated):
            product=Product.objects.get(pk=pk)
            present=False
            result=Cart.objects.filter(Q(product=product) & Q(user=request.user))
            if(result):
                present=True
            return render(request,"app/productdetail.html",{
            "product":product,
            "present":present
            
    })
        else:
            product=Product.objects.get(pk=pk)
            present=False
            result=Cart.objects.filter(Q(product=product))
            return render(request,"app/productdetail.html",{
            "product":product,
            "present":present
            
    })
    if(request.method=='POST'):
        prod=Product.objects.get(pk=pk)
        usr=request.user
        present=False
        # result=Cart.objects.filter(product=prod)
        result=Cart.objects.filter(Q(product=prod) & Q(user=request.user))
        if(result):
            present=True
        reg=Cart(user=usr,product=prod)
        reg.save()
        # return render(request,"app/productdetail.html",{
        #     "product":prod,
        #     "present":present
        # })
        return redirect(reverse('productdetail', kwargs={'pk': pk}))
        
    
    
def buynow(request):
    return render(request,"app/buynow.html")

def mobile(request):
    products=Product.objects.filter(category="Mobiles")
    # print(len(products))
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })
    
def laptop(request):
    products=Product.objects.filter(category="Laptops")
    # print(len(products))
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })


def mensTopWear(request):
    products=Product.objects.filter(category="Men's Top Wear")
    # print(len(products))
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })
    
    
def mensBottomWear(request):
    products=Product.objects.filter(category="Men's Bottom Wear")
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })
    
    
def womensTopWear(request):
    products=Product.objects.filter(category="Women's Top Wear")
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })
    
    
    
def womensBottomWear(request):
    products=Product.objects.filter(category="Women's Bottom Wear")
    # print(products[0].category)
    cat=products[0].category
    return render(request,"app/products.html",{
        "products":products,
        "category":cat
    })

def orderplaced(request):
    return render(request,"app/orderplaced.html")