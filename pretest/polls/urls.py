from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    path('stadium', views.stadium_list),
    path('<int:pk>/', views.stadium_detail),
    path('review', views.review_list),
    path('<int:pk>/', views.review_detail),
]