from django.shortcuts import render
from django.shortcuts import render
from .serializers import VendorSerializer,UnitSerializer,PurchaseSerializer,InventorySerializer,ProductSerializer,SaleSerializer
from rest_framework import viewsets
from .models import Vendor,Sale,Purchase,Unit,Product,Inventory
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.

class VendorView(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class =  VendorSerializer
    # filter_backends = [SearchFilter,OrderingFilter]
    # search_fields = ['title','first_name','last_name','email']

class UnitView(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer 

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class PurchaseView(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer 

class SaleView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer 

class InventoryView(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer 

       
   

