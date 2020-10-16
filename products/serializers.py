from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id',
                  'title',
                  'description',
                  'type',
                  'ram',
                  'color',
                  'processor',
                  'hdCapacity',
                  'screenSize')
