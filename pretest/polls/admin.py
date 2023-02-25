from django.contrib import admin
# Register your models here.

from .models import Review
from .models import Stadium

class PostAdmin(admin.ModelAdmin):
    list_display = ('totalrating', 'foodrating', 'accessratinng', 'visibilityrating', 'passionrating', 'created_at', 'updated_at', 'user', 'stadium')

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','team','place','image','created_at','avetotalrating','avefoodrating','aveaccessrating','avevisibilityrating','avepassionrating')

admin.site.register(Review)
admin.site.register(Stadium)