from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.health_check, name="health"),
    path("register/", views.Register.as_view(), name="register"),
    path("signin/", views.Signin.as_view(), name="signin"),
    path("signout/", views.Signout.as_view(), name="signout"),
]
