from django.shortcuts import render
from django.conf import settings
from django.views import generic
from .models import Product


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ProductListView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 100
