


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, LikesViewSet, PostViewsViewSet, CategoryViewSet

router = DefaultRouter()
router.register("blogs", BlogViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikesViewSet)
router.register('postviews', PostViewsViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
