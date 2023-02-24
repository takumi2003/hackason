from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stadium_images')
    created_at = models.DateTimeField(auto_now_add=True)
    totalrating = models.IntegerField(default=0,)
    foodrating = models.IntegerField(default=0,)
    accessrating = models.IntegerField(default=0,)
    visibilityrating = models.IntegerField(default=0,)
    passionrating = models.IntegerField(default=0,)


class Review(models.Model):
    totalrating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    foodrating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    accessrating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    visibilityrating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    passionrating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

