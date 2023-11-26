from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .temp_data import flower_data

from django.http import HttpResponseRedirect
from django.urls import reverse

def detail_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    context = {'flower': flower_data[flower_id - 1]}
    return render(request, 'flowers/detail.html', context)

def list_flowers(request):
    context = {"flower_list": flower_data}
    return render(request, 'flowers/index.html', context)

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