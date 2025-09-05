from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'owner', 'title', 'content', 'price'
        ]
        read_only_fields = ['owner',]  # Владелец проставляется автоматически