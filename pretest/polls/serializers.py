from rest_framework import serializers
from .models import Stadium
from .models import Review

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'team',
            'place',
            'image',
            'created_at',
            'avetotalrating',
            'avefoodrating',
            'aveaccessrating',
            'avevisibilityrating',
            'avepassionrating',
        )
        model = Stadium

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'totalrating',
            'foodrating', 
            'accessratinng', 
            'visibilityrating', 
            'passionrating', 
            'created_at', 
            'updated_at', 
            'user', 
            'stadium'
        )
        model = Review