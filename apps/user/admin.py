from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

class CustomUser(UserAdmin):
    #adjustments
    ...


# Register your models here.
admin.site.register(models.User, CustomUser)