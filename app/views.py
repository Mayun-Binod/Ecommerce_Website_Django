from django.shortcuts import render
from datetime import datetime
from app.models import *
from django.views import View
from .models import User
from .forms import CustomerRegistrationForm

# def home(request):
#  context={"date":datetime.now}
#  return render(request, 'app/home.html',context)
class ProductView(View):
 def get(self,request):
  mobile=Product.objects.filter(category='MB')
  laptop=Product.objects.filter(category='LP')
  topwears=Product.objects.filter(category='TW')
  bottomwears=Product.objects.filter(category='BW')
  return render(request, 'app/home.html',{'mobile':mobile,'laptop':laptop,'topwears':topwears,'bottomwears':bottomwears})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 if data==None:
  mobiles=Product.objects.filter(category='MB')
 elif data=='oneplus' or data=='samsung':
  mobiles=Product.objects.filter(category='MB').filter(brand=data)
 elif data=='below':
  mobiles=Product.objects.filter(category='MB').filter(discounted_price__lt=1500)
 elif data=='above':
  mobiles=Product.objects.filter(category='MB').filter(discounted_price__gt=1500)
 return render(request, 'app/mobile.html',{"mobiles":mobiles})

def laptop(request,data=None):
 if data==None:
  laptops=Product.objects.filter(category="LP")
 elif data=='Apple' or data=="lenovo":
  laptops=Product.objects.filter(category='LP').filter(brand=data)
 elif data=="below":
  laptops=Product.objects.filter(category="LP").filter(discounted_price__lt=8000)
 elif data=="above":
  laptops=Product.objects.filter(category="LP").filter(discounted_price__gt=8000)
 return render(request, 'app/laptop.html',{"laptops":laptops})

def topwears(request,data=None):
 if data==None:
  tops=Product.objects.filter(category="TW")
 elif data=='lee' or data=="jett":
  tops=Product.objects.filter(category='TW').filter(brand=data)
 elif data=="below":
  tops=Product.objects.filter(category="TW").filter(discounted_price__lt=250)
 elif data=="above":
  tops=Product.objects.filter(category="TW").filter(discounted_price__gt=250)
 return render(request, 'app/topwears.html',{"tops":tops})


def bottomwears(request,data=None):
 if data==None:
  bottoms=Product.objects.filter(category="BW")
 elif data=='nick' or data=="zebra":
  bottoms=Product.objects.filter(category='BW').filter(brand=data)
 elif data=="below":
  bottoms=Product.objects.filter(category="BW").filter(discounted_price__lt=500)
 elif data=="above":
  bottoms=Product.objects.filter(category="BW").filter(discounted_price__gt=500)
 return render(request, 'app/bottomwears.html',{"bottoms":bottoms})


def login(request):
 return render(request, 'app/login.html')

class  CustomerRegistrationView(View):
 def get(self,request):
  form=CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html',{"form":form})
 
 def post(self,request):
  form=CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
  return render(request, 'app/customerregistration.html',{"form":form})

def checkout(request):
 return render(request, 'app/checkout.html')
