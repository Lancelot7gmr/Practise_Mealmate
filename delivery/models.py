from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username} -  {self.email}' 
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(default="https://static.vecteezy.com/system/resources/previews/052/792/818/non_2x/restaurant-logo-design-vector.jpg")
    cuisine = models.CharField(max_length = 20, default="Add type of cuisine here")
    rating = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.cuisine} - {self.rating}"