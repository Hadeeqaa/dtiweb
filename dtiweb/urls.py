from django.urls import path
from .views import ClothesView,UserView

urlpatterns = [
    path('clothes/', ClothesView.as_view()),
    path('register/', UserView.as_view())
]