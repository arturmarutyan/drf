from django.shortcuts import render
from products.models import Product
from django.http import JsonResponse
from rest_framework.response import Response
from products.serializers import ProductSerializer
import json
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def api_home(request, *args, **kwargs):
    if request.method == 'GET':
        instance = Product.objects.all().order_by('?').all()
        data = {}
        if instance:
            data = ProductSerializer(instance, many=True).data
        return Response(data)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response({'invalid' : 'wrong data format'}, status=400)
    # serialization
    # model_data = Product.objects.all().order_by('?').first()
    # data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
    #     data = model_to_dict(model_data, fields=['id', 'title', 'content'])
    # return JsonResponse(data)
