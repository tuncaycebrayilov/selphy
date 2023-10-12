from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from blog.models import blog
from shop.models import product
from api.serializers import BlogSerializer, ShopSerializer

class BlogApiView(APIView):
    serializer_class = BlogSerializer
    permisson_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kvargs):
        if kvargs.get('pk'):
            obj = blog.objects.get(pk=kvargs.get('pk'))
            serializer = self.serializer_class(obj)

        else:
            all_blogs = blog.objects.all()
            serializer = self.serializer_class(all_blogs, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ShopApiView(APIView):
    serializer_class = ShopSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kvargs):
        if kvargs.get('pk'):
            obj = product.objects.get(pk=kvargs.get('pk'))
            serializer = self.serializer_class(obj)
        
        else:
            all_products = product.objects.all()
            serializer = self.serializer_class(all_products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)