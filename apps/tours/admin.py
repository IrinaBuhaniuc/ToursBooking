from django.contrib import admin

from . import models

class CustomTour(admin.ModelAdmin):
    list_display = (
        'name', 
        'category_name',
        'location',
        'price_euro',
        'get_description',
        
        )
    @admin.display(description = "Price")
    def price_euro(self,obj):
        return f"{obj.price} EURO"
    
    @admin.display(description = "Description")
    def get_description(self,obj):
        if len(obj.description)>50:
            return f"{obj.description[:50]}..."
    
        return f"{obj.description[:50]}"
    
    @admin.display(description = "Category")
    def category_name(self,obj):
        return obj.cat_id.name

class CustomCategory(admin.ModelAdmin):
    list_display= (
        'name',
    )
 
class CustomTourReview(admin.ModelAdmin):
    list_display = (
        'get_tour_name',
        'review'
    )
    @admin.display(description="Tour")
    def get_tour_name(self,obj):
        return obj.tour_id.name  
    
class CustomerRating(admin.ModelAdmin):
    list_display = [
        'get_tour_name',
        'rate'
    ]
    @admin.display(description="Tour")
    def get_tour_name(self,obj):
        return obj.tour_id.name  
    
class CustomerBookingTour(admin.ModelAdmin):
    list_display = [
        'get_user_name',
        'get_tour_name',
        'get_start_date'
    ]
    @admin.display(description="Tour")
    def get_tour_name(self,obj):
        return obj.tour_id.name 

    @admin.display(description="Start Date")
    def get_start_date(self,obj):
        return obj.tour_id.start_date 
    
    @admin.display(description="User")
    def get_user_name(self,obj):
        return obj.user_id.username 
    
# Register your models here.
admin.site.register(models.Category,CustomCategory)
admin.site.register(models.Tour, CustomTour)
admin.site.register(models.TourReview, CustomTourReview)
admin.site.register(models.Rating, CustomerRating)
admin.site.register(models.BookingTour, CustomerBookingTour)
