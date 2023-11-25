from django.contrib import admin

from .models import Flower, Review, List, Provider

admin.site.register(Flower)
admin.site.register(Review)
admin.site.register(List)
admin.site.register(Provider) 