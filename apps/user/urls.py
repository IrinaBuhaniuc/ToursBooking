from django.urls import path
from . import views

urlpatterns = [
    
    path("signup/", views.add_user, name = "add-user"),
    path('login/', views.login_view, name="login-view"),
    path('profile/', views.profile, name="profile"),
]
