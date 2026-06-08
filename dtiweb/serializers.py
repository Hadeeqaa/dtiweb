from rest_framework import serializers
from .models import Clothes

class InputUserData(serializers.Serializer):
    tier= serializers.ChoiceField(choices = Clothes.Tier.choices)
    count = serializers.IntegerField(min_value=1 , max_value=10)
 
class OutputUserData(serializers.Serializer):
    item = serializers.ImageField()

    