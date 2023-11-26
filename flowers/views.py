from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse, reverse_lazy

from .models import Flower, Review, List, Provider 
from .forms import FlowerForm, ReviewForm, ProviderForm

from django.shortcuts import render, get_object_or_404

from django.views import generic

def detail_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    context = {'flower': flower_data[flower_id - 1]}
    return render(request, 'flowers/detail.html', context)

def list_flowers(request):
    context = {"flower_list": flower_data}
    return render(request, 'flowers/index.html', context)

def create_flower(request):
    flower_form = FlowerForm(request.POST)
    provider_form = ProviderForm(request.POST)
    flower = flower_form.save()
    context = {'flower_form': flower_form}
    return render(request, 'flowers/create.html', context)

def update_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    form = FlowerForm(
            initial={
                'name': flower.name,
                'release_year': flower.release_year,
                'poster_url': flower.poster_url
            })
    flower.save()
    context = {'flower': flower, 'form': form}
    return render(request, 'flowers/update.html', context)

def delete_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    flower.delete()
    context = {'flower': flower}
    return render(request, 'flowers/delete.html', context)

class ListListView(generic.ListView):
    model = List
    template_name = 'flowers/lists.html'

class ListCreateView(generic.CreateView):
    model = List
    template_name = 'flowers/create_list.html'
    fields = ['name', 'author', 'flowers']
    success_url = reverse_lazy('flowers:lists')

class FlowerListView(generic.ListView):
    model = Flower
    template_name = 'flowers/index.html'













'''
def create_review(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            flower=flower)
            review.save()
            return HttpResponseRedirect(
                reverse('flowers:detail', args=(flower_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'flower': flower}
    return render(request, 'flowers/review.html', context)

def search_flowers(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "flower_list": [
                m for m in flower_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'flowers/search.html', context)

def create_flower(request):
    if request.method == 'POST':
        flower_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('flowers:detail', args=(len(flower_data), )))
    else:
        return render(request, 'flowers/create.html', {})
        flower_form = FlowerForm()
        provider_form = ProviderForm()
    context = {'flower_form': flower_form, 'provider_form': provider_form}
    return render(request, 'flowers/create.html', context)


def update_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)

    if request.method == "POST":
        form = FlowerForm(request.POST)
        if form.is_valid():
            flower.name = form.cleaned_data['name']
            flower.release_year = form.cleaned_data['release_year']
            flower.poster_url = form.cleaned_data['poster_url']
            flower.save()
            return HttpResponseRedirect(
                reverse('flowers:detail', args=(flower.id, )))
    else:
        form = FlowerForm(
            initial={
                'name': flower.name,
                'release_year': flower.release_year,
                'poster_url': flower.poster_url
            })

    context = {'flower': flower, 'form': form}
    return render(request, 'flowers/update.html', context)

def delete_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)

    if request.method == "POST":
        flower.delete()
        return HttpResponseRedirect(reverse('flowers:index'))

    context = {'flower': flower}
    return render(request, 'flowers/delete.html', context)

    #from .models import Flower, Review, List, Provider


from django.http import HttpResponse
from .temp_data import flower_data
'''
