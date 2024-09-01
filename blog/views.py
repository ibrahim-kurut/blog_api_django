from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Blog, Comment, Likes, PostViews, Category

from .serializers import BlogSerializer, CommentSerializer, LikesSerializer, PostViewsSerializer, CategorySerializer

from rest_framework import viewsets, status

from rest_framework.response import Response


from .permissions import IsStaffOrReadOnly , IsOwnerOrStaff, IsOwnerOrReadOnly

from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('-publish_date')
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
    # Automatically assign the owner who created the post.
        serializer.save(user=self.request.user)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # PostView oluşturuluyor
        PostViews.objects.create(blog=instance, user=request.user if request.user.is_authenticated else None)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# ============== send created msg ==============
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Post created successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_201_CREATED
                )

# ============== send update msg ==============
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 
        return Response(
            {
                'message': 'Post updated successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_200_OK
                )

# ============== send deleted msg ==============
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                'message': 'Post deleted successfully',
                },status=status.HTTP_204_NO_CONTENT)





class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


    # ============== send created msg ==============
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'comment created successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_201_CREATED
                )


    # ============== send update msg ==============
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 
        return Response(
            {
                'message': 'comment updated successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_200_OK
                )

    # ============== send deleted msg ==============
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                'message': 'comment deleted successfully',
                },status=status.HTTP_204_NO_CONTENT)
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]




    # ============== send created msg ==============
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'category created successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_201_CREATED
                )


    # ============== send update msg ==============
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 
        return Response(
            {
                'message': 'category updated successfully',
                "data":serializer.data
                }, 
                status=status.HTTP_200_OK
                )

    def destroy(self, request, *args, **kwargs):
        print("Destroy method called")
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                'message': 'category deleted successfully',
            },
            status=status.HTTP_200_OK
        )



    

class LikesViewSet(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer


class PostViewsViewSet(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer



