from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                                   # Homepage
    path('best-bf/', views.best_bf, name='best_bf'),                     # Best BF page
    path('personality/', views.personality, name='personality'),          # Personality section
    path('physical-traits/', views.physical_traits, name='physical_traits'), # Physical traits section
    path('hobbies/', views.hobbies, name='hobbies'),                     # Hobbies section
    path('birthday-card/', views.birthday_card, name='birthday_card'),    # Birthday card page
]