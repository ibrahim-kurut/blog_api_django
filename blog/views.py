from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Blog, Comment, Likes, PostViews, Category

from .serializers import BlogSerializer, CommentSerializer, LikesSerializer, PostViewsSerializer, CategorySerializer



# Create your views here.

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('-publish_date')
    serializer_class = BlogSerializer
    

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class LikesViewSet(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer


class PostViewsViewSet(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


