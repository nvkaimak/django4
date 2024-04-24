from rest_framework import serializers

from main.models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price']


class ProductDetailsSerializer(serializers.ModelSerializer):
    comments = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'comments']

