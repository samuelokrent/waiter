from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.order_list, name='order_list'),
    url(r'^delete/(?P<pk>\d+)$', views.order_claim, name='order_claim'),
]
