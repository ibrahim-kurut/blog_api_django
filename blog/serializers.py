

from rest_framework import serializers
from .models import Blog, Comment, Likes, PostViews, Category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


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

    # count comments for each post
    comments_count = serializers.SerializerMethodField()
    # View all comments related to post
    comments = CommentSerializer(many=True, read_only=True)

    # Calculate the count of comments for each post
    def get_comments_count(self, obj):
        return obj.comments.count()

    # show the count of likes for each post
    likes_count = serializers.SerializerMethodField()
    def get_likes_count(self, obj):
        return obj.likes.count()


    # show the count of likes for each post
    blogView = serializers.SerializerMethodField()
    def get_blogView(self, obj):
        return obj.blogView.count()



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
