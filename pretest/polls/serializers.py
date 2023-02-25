from rest_framework import serializers
from .models import Stadium
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
            'accessrating', 
            'visibilityrating', 
            'passionrating', 
            'created_at', 
            'updated_at', 
            'user', 
            'stadium'
        )
        model = Review

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')