# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from waiter.models import Order

def index(request):
    return HttpResponse(render_to_string("index.html", context={"value":"there"}))

def order_list(request, template_name='orders/order_list.html'):
    orders = Order.objects.all()
    data = {}
    data['object_list'] = orders
    return render(request, template_name, data)

def order_claim(request, pk, template_name='orders/order_confirm_claim.html'):
    order = get_object_or_404(Order, pk=pk)    
    if request.method=='POST':
        order.delete()
        return redirect('order_list')
    return render(request, template_name, {'object': order})