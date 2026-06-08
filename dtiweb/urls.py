from django.urls import path
from .views import ClothesView

urlpatterns = [
    path('clothes/', ClothesView.as_view()),
]