

from rest_framework import serializers
from .models import Blog, Comment, Likes, PostViews, Category



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


    # show category name in post 
    category_name = serializers.SerializerMethodField()
    def get_category_name(self, obj):
        return obj.category.name

   

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class PostViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostViews
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
