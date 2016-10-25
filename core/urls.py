from django.conf.urls import url, include
from . import views
from core.views import ProductListView, ProductCreateView, ProductUpdateView,\
ProductDetailView, ProductDeleteView, AutoComplete, HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^list/$', ProductListView.as_view(), name='product_list'),
    url(r'^add/$', ProductCreateView.as_view(), name='product_add'),
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^product/editar/(?P<pk>\d+)/$', ProductUpdateView.as_view(), name='product_update'),
    url(r'^product/delete/(?P<pk>\d+)/$', ProductDeleteView.as_view(), name='product_delete'),
    url(r'autocomplete/$',AutoComplete.as_view(), name='product-auto'),

]
