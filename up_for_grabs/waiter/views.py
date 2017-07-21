# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from waiter.models import Order

import json
from django.utils import timezone

def index(request):
    return HttpResponse(render_to_string("index.html", context={"value":"there"}))

def order_list_json(request):
    orders = Order.objects.all()
    dictionaries = [ obj.as_dict() for obj in orders ]
    return HttpResponse(json.dumps(dictionaries), content_type='application/json')

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

def order_create(request):
    try:
        order = json.loads(request.body)
        print('order_create: ', order)

        o = Order(description=order['description'],
                name=order['name'],
                office=order['office'],
                arrival_time = timezone.now())
        o.save()
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
    return HttpResponse(status=500)