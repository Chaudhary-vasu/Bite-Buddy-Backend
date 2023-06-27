from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class MealsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealsItems
        fields = '__all__'
        
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
