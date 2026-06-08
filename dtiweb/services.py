from .models import Clothes

def outputting_service(tier,count):
    rando=Clothes.objects.filter(tier=tier).order_by('?')[:count]
    return rando