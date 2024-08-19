from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home),
    path("login",views.user_login,name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("register",views.register.as_view(),name="register"),
    path("cart",views.cart,name="cart"),
    path("pluscart",views.plus_cart,name="plus_cart"),
    path("minuscart",views.minus_cart,name="minus_cart"),
    path("delete/<int:prod_id>",views.remove_cart,name="remove_cart"),
    path("profile",views.profile.as_view(),name="profile"),
    path("address",views.address,name="address"),
    path("orders",views.orders,name="orders"),
    path("changepassword",views.changepassword,name="changepassword"),
    path("checkout",views.checkout,name="checkout"),
    path("payment",views.payment,name="payment"),
    path("mobile",views.mobile,name="mobile"),
    path("laptop",views.laptop,name="laptop"),
    path("<str:cat>/<int:pk>",views.productdetail,name="productdetail"),
    path("productdetail/<int:pk>",views.productdetail,name="productdetail"),
    path("buynow",views.buynow,name="buynow"),
    path("mens-top-wear",views.mensTopWear,name="mensTopWear"),
    path("mens-bottom-wear",views.mensBottomWear,name="mensBottomWear"),
    path("womens-top-wear",views.womensTopWear,name="womensTopWear"),
    path("womens-bottom-wear",views.womensBottomWear,name="womensBottomWear"),
    path("orderplaced",views.orderplaced,name="orderplaced")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
