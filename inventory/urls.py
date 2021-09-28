
from django.contrib import admin
admin.autodiscover()
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from enroll.views import VendorView,UnitView,ProductView,PurchaseView,SaleView,InventoryView

router = routers.DefaultRouter()
router.register('vendor', VendorView)
# router.register('employee/id', EmployeeView)
router.register('unit', UnitView)
router.register('product', ProductView)
router.register('purchase', PurchaseView)
router.register('sale', SaleView)
router.register('inventory', InventoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   
]