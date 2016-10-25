from django.conf.urls import url, include
from . import views
from core.views import ProductListView


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='home'),
]
