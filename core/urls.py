from django.conf.urls import url, include
from . import views
from core.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='home'),
    url(r'^add/$', ProductCreateView.as_view(), name='product_add'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^product/editar/(?P<pk>\d+)/$', ProductUpdateView.as_view(), name='product_update'),
     url(r'^product/delete/(?P<pk>\d+)/$', ProductDeleteView.as_view(), name='product_delete'),

]
