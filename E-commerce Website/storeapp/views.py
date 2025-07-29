from django.shortcuts import render,redirect
from .models import Products

from .serializers import ProductSerializer

#serializer_view
from rest_framework.response import Response
#permissions,viewsets 
from rest_framework import generics ,status  #using generics
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class Product_list(generics.ListCreateAPIView):
    queryset=Products.objects.all() #viewset ->api,database data
    serializer_class=ProductSerializer
     
    # Delete all in models
    def delete(self,request,*args,**kwargs):
        Products.object.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Update(put,patch), delete 
class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'




# Create your views here.
def home(request):
    products=Products.objects.all()
    return render(request,'home.html',{'products':products})


def webpage(request):
    products=Products.objects.all()
    return render(request,'demo.html',{'products':products})

def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})







#Athentication
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,(" successfull.. login"))
            return redirect('home')
        else:
            messages.success(request,("details Not matches"))
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("logout is successfull.."))
    return redirect('login_user')