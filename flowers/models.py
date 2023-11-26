from django.db import models
from django.conf import settings

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.release_year})'

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Provider(models.Model):
    flower = models.OneToOneField(
        Flower,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    service = models.CharField(max_length=255, blank=True)
    has_flat_price = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=True,
                                blank=True)

    def __str__(self):
        return f'{self.service} @ {self.price if self.price else "flat"}'

class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    flowers = models.ManyToManyField(Flower)

    def __str__(self):
        return f'{self.name} by {self.author}'
    

