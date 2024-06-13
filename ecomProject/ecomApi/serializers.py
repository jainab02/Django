from rest_framework import serializers
from .models import *
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields='__all__'
class CustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields='__all__'