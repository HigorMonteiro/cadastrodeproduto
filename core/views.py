from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.conf import settings
from django.views import generic
from .models import Product
import json


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ProductListView(LoginRequiredMixin, generic.ListView):
    template_name = 'core/product_list.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 100


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/product_form.html'
    model = Product
    fields = ['code', 'product']
    success_url = reverse_lazy('core:product_list')


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['code', 'product']
    success_url = reverse_lazy('core:product_list')


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('core:product_list')


class AutoComplete(generic.View):
    def get(self, request, *args, **kwargs):
        query = Q()
        if request.GET.get('term', False):
            query = Q(name__icontains=request.GET['term'])
        products = Product.objects.filter(query)
        dados = [{'id': product.id, 'name': product.product} for product in products]
        mimetype = "application/json;charset=UTF-8"
        js = json.dumps(dados, ensure_ascii=False).encode('utf8')
        return HttpResponse(js, mimetype)
