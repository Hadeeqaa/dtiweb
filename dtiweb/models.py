from django.db import models


class Clothes(models.Model):
    name = models.CharField(max_length=100)
    item = models.ImageField(upload_to='clothes/')
    class Tier(models.TextChoices):
        NONVIP = 'NON-VIP','Non-VIP'
        VIP = 'VIP','VIP'
    tier = models.CharField(max_length=10,
        choices= Tier.choices,
        default = Tier.NONVIP)
    
    def __str__(self):
        return f"{self.name} - {self.tier} " 
    