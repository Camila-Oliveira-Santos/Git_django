from django.forms import ModelForm
from .models import Flower, Review, Provider


class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = [
            'name',
            'especie',
            'poster_url',
            'curiosidade',
        ]
        labels = {
            'name': 'Título',
            'especie': 'Espécie',
            'poster_url': 'URL do Poster',
            'curiosidade': 'Curiosodade',
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = [
            'service',
            'has_flat_price',
            'price',
        ]
        labels = {
            'service': 'Serviço de Streaming',
            'has_flat_price': 'FLAT?',
            'price': 'Preço',
        } 