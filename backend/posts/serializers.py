from rest_framework import serializers
from .models import Categories,Post,Comment

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=['id','category']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        read_only_fields=['author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fiels=['id','post','contents']