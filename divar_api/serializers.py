from rest_framework import serializers
from .models import House, HouseSpecifications, Seller


class HouseSerializer (serializers.ModelSerializer):
    specifications = HouseSpecifications()
    seller = Seller()

    class Meta:
        model = House
        fields = [
            'title',
            'seller',
            'total_price',
            'price_per_meter',
            'agency',
            'floor',
            'specifications',
            'city',
            'address',
            'description'
        ]
