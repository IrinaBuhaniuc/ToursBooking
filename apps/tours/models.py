from django.db import models
from apps.core.models import  CreatedModifiedAtDateTimeBase
from .validators import rating_range

# Create your models here.
class Category(CreatedModifiedAtDateTimeBase):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    
class Tour(CreatedModifiedAtDateTimeBase):
    cat_id = models.ForeignKey("tours.Category", null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    def __str__(self):
        return self.name
    
class TourReview(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    tour_id = models.ForeignKey("tours.Tour", on_delete=models.CASCADE)
    review = models.TextField()
    
    def __str__(self):
        return self.review
    
class Rating(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    tour_id = models.ForeignKey("tours.Tour", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[rating_range])
    
    def username(self):
        return self.user_id.username
  
    def resource_title(self):
        return self.tour_id.name
    
class BookingTour(CreatedModifiedAtDateTimeBase):
    user_id = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    tour_id = models.ForeignKey("tours.Tour", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.tour_id.name
    
    
