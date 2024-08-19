from django.contrib import admin

# Register your models here.
from .models import Customer
admin.site.register(Customer)

from .models import Product
admin.site.register(Product)

from .models import Cart
admin.site.register(Cart)

from .models import OrderPlaced
admin.site.register(OrderPlaced)