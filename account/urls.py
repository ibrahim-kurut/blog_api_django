from django.urls import path

from .views import Register, Users



# register endpoint = api/users/register/
urlpatterns = [
    path('register/', Register.as_view()),
    path('userinfo/', Users.as_view()),    # api/users/userinfo/
]