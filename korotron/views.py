from django.db.models import Count, F, Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


def index(request):
    aboutus = AboutUS.objects.filter(is_published=True)
    carousel = Action.objects.filter(is_published=True)
    context = {
        'aboutus': aboutus,
        'carousel': carousel,
    }
    return render(request, 'main/index.html', context)


def get_service(request, category_id):
    services = Services.objects.filter(category_id=category_id, is_published=True)
    Category = CategoryService.objects.filter(pk=category_id)
    context = {
        'services': services,
        'Category': Category,
    }
    return render(request, 'main/services.html', context)


class Search(ListView):
    template_name = 'main/search.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Services.objects.filter(Q(title__icontains=self.request.GET.get('s'))
                                       | Q(description__icontains=self.request.GET.get('s'))).order_by('category__title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = CategoryService.objects.all()
        return context



def test(request):
    return render(request, 'main/test.html')