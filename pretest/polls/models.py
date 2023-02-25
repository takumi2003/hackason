from django.db import models
from django.contrib.auth.models import User

# Create your models here


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='stadium_images')
    created_at = models.DateTimeField(auto_now_add=True)
    avetotalrating = models.FloatField(default=0)
    avefoodrating = models.FloatField(default=0)
    aveaccessrating = models.FloatField(default=0)
    avevisibilityrating = models.FloatField(default=0)
    avepassionrating = models.FloatField(default=0)
    def __str__(self):
        return self.name



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
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        stadium_reviews = Review.objects.filter(stadium=self.stadium)
        if stadium_reviews.count() > 0:
            totalrating_avg = stadium_reviews.aggregate(models.Avg('totalrating'))['totalrating__avg']
            foodrating_avg = stadium_reviews.aggregate(models.Avg('foodrating'))['foodrating__avg']
            accessrating_avg = stadium_reviews.aggregate(models.Avg('accessrating'))['accessrating__avg']
            visibilityrating_avg = stadium_reviews.aggregate(models.Avg('visibilityrating'))['visibilityrating__avg']
            passionrating_avg = stadium_reviews.aggregate(models.Avg('passionrating'))['passionrating__avg']
            self.stadium.avetotalrating = totalrating_avg
            self.stadium.avefoodrating = foodrating_avg
            self.stadium.aveaccessrating = accessrating_avg
            self.stadium.avevisibilityrating = visibilityrating_avg
            self.stadium.avepassionrating = passionrating_avg
            self.stadium.save()

