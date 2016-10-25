from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 100


class ProductCreateView(generic.CreateView):
    template_name = 'core/product_form.html'
    model = Product
    fields = ['code', 'product']
    success_url = reverse_lazy('core:home')


class ProductDetailView(generic.DetailView):
    model = Product


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ['code', 'product']
    success_url = reverse_lazy('core:home')


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('core:home')
