

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

    # show the user name in post
    username = serializers.SerializerMethodField()
    def get_username(self, obj):
        return obj.user.username

    # show the comments count for each post
    comments_count = serializers.SerializerMethodField()
    def get_comments_count(self, obj):
        return Comment.objects.filter(blog=obj).count()

   

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
