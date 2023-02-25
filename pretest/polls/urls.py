from django.urls import path
from . import views
from .views import LoginView,LogoutView,UserCreate

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('users/', UserCreate.as_view()),
    path('stadium', views.StadiumList.as_view()),
    path('<int:pk>/', views.StadiumDetail.as_view()),
    path('review', views.ReviewList.as_view()),
    path('<int:pk>/', views.ReviewDetail.as_view()),
]