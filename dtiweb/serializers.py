from rest_framework import serializers
from .models import Userdti,Clothes

class InputUserData(serializers.Serializer):
    tier= serializers.ChoiceField(choices = Userdti.Tier.choices)
    count = serializers.IntegerField(min_value=1 , max_value=10)
 
class OutputUserData(serializers.Serializer):
    item = serializers.ImageField()

class UserRegistrationData(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(min_length=8)