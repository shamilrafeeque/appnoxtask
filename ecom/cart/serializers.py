from rest_framework import serializers
from .models import cart

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields=('item','user','quantity')