from django.shortcuts import render
from rest_framework.decorators import permission_classes,api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializers
from rest_framework.response import Response
from .models import cart
from accounts.models import Account
from products.models import Products
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Addcart(request,id):
    try:
        products = Products.objects.get(id=id)
        user=request.user
        users=Account.objects.get(username=user)
        #if the cart is exist on that product add quantitiy+1
        if user==users:
            if cart.objects.filter(item=products).exists():
                kk=cart.objects.get(item=id)
                kk.quantity +=1
                kk.save()
                
                
            else:
                # #if the cart is does not exist create a new cart item
                carts=cart.objects.create(item=products,user=users,quantity=1,is_active=True)
                carts.save()
            
    except:
        return Response("please product is not available")
    carts=cart.objects.filter(user=user)
    serializer = CartSerializers(carts,many=True)
    return Response(serializer.data)