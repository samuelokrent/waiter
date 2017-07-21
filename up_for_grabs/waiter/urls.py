from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orders$', views.order_list_json, name='order_list_json'),
    url(r'^testlist$', views.order_list_json, name='order_list'),
    url(r'^claim/(?P<pk>\d+)$', views.order_claim, name='order_claim'),
    url(r'^create$', views.order_create, name='order_create'),
]
