from django.urls import path

from .views import Register, Users, Logout



# register endpoint = api/users/register/
urlpatterns = [
    path('register/', Register.as_view()),
    path('userinfo/', Users.as_view()),    # api/users/userinfo/
    path('logout/', Logout.as_view()),  # api/users/logout/
]