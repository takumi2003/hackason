
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Stadium
from .models import Review
from .serializers import StadiumSerializer
from .serializers import ReviewSerializer
from rest_framework import status
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
class StadiumList(APIView):
    def get(self, request):
        stadiums = Stadium.objects.all()
        serializer = StadiumSerializer(stadiums, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = StadiumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StadiumDetail(APIView):
    def get_object(self, pk):
        try:
            return Stadium.objects.get(pk=pk)
        except Stadium.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        stadium = self.get_object(pk)
        serializer = StadiumSerializer(stadium)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        stadium = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = StadiumSerializer(stadium, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk):
        stadium = self.get_object(pk)
        stadium.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)

class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.body.decode('utf-8')
        if not data:
            return JsonResponse({'error': 'Request body is empty'}, status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(data)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        review = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)


    
#ここからログイン機能

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


