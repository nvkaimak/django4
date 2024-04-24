from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    product = Product.objects.all()
    ser = ProductListSerializer(product, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try :
            product = Product.objects.get(id=product_id)
            ser = ProductDetailsSerializer(product)
            return Response(ser.data)
        except Product.DoesNotExist:
            return Response(status=404)




class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        mark = request.query_params.get('mark')
        reviews = Review.objects.filter(product_id=product_id)

        if mark:
            reviews = reviews.filter(mark=mark)

        ser = ReviewSerializer(reviews, many=True)
        return Response(ser.data)