from django.contrib import admin
from .models import  Resturant

# Register your models here.
class ResturantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'image')

admin.site.register(Resturant, ResturantAdmin)