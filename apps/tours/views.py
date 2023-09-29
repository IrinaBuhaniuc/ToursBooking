from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

from apps.tours.models import BookingTour, Tour, TourReview, Rating



# Create your views here.
def homepage(request):
    all_tours = Tour.objects.all()
    # tours_list = ''
    # for tour in all_tours:
    #     tours_list += f'<li><a href="{reverse("tours-details", args= [tour.id])}">{tour}</a></li>'
    # response_data = f'<ul> {tours_list} </ul>'
    # return HttpResponse(response_data)
    context = {
        'tours_list': all_tours
    }
    return render(request, "tours/homepage.html", context)

def tours_list(request):
    all_tours = Tour.objects.all()
    context = {
        'tours_list': all_tours
    }
    return render(request, "tours/tours_list.html", context)

def tour_details(request,id):

    tour = (
        Tour.objects.select_related('cat_id')
        .get(pk=id)
        )
    review = TourReview.objects.filter(tour_id_id=id)
    
    avg_rate = Rating.objects.filter(tour_id_id=tour.id).aggregate(Avg('rate'))
    #average = res.rating_set.aggregate(Avg('rate'))
    
    context = {
        'tour': tour,
        'reviews': review,
        'avg_rate': avg_rate['rate__avg']

               }
    return render(request=request, 
                  template_name='tours/tour_details.html',
                  context= context)
  
@login_required  
def booked_tours(request):
    user = request.user
    booked_tours = BookingTour.objects.filter(user_id = user)
    context={
        'booked_tours':booked_tours
    }
    
    return render(request, "user/profile.html", context)
   