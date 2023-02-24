from django.contrib import admin
# Register your models here.

from .models import Stadium

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'place', 'imgae', 'created_at')

admin.site.register(Stadium)