from rest_framework import serializers
from .models import Vendor,Sale,Purchase,Unit,Product,Inventory

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=('id','full_name','photo','address','status')



class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields=('id','title','short_name')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','title','details','unit','photo') 


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields=('id','product','vendor','qty','price','total_amt','pur_date') 


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        fields=('id','product','qty','price','total_amt','sale','customer_name','descriptioncustomer_mobile','customer_address')  


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields=('id','product','purchase','sale','pur_qty','sale_qty','total_bal_qty')  





                