from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     post = Post.objects.create(**validated_data)
    #     Category.objects.create(post=post, **category_data)
    #     return post
