from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        # print("Oky")
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    return {'cart_item_count': cart_count}
