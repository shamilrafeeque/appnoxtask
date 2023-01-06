from django.shortcuts import render
from rest_framework import exceptions, generics, status
from .models import Products
from .serializers import ProductSerializer
# Create your views here.
class ProductList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer