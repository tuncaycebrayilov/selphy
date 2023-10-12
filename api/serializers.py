from rest_framework import serializers

from blog.models import blog
from shop.models import product

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__' 