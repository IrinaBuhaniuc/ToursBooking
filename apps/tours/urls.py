from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name = "home-page"),
    path("tours/<int:id>", views.tour_details, name = "tours-details"),
    path("tours/", views.tours_list, name = "tours-list"),
    path("booked_tours", views.booked_tours, name="booked-tours")
    
]
