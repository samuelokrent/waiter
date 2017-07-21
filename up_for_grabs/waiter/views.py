# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from waiter.models import Order

import json
from django.utils import timezone

def index(request, template_name='orders/index.html'):
    return render(request, template_name, {})

def order_list_json(request):
    orders = Order.objects.all()
    dictionaries = [ obj.as_dict() for obj in orders ]
    return HttpResponse(json.dumps(dictionaries), content_type='application/json')

def order_list(request, template_name='orders/order_list.html'):
    orders = Order.objects.all()
    data = {}
    data['object_list'] = orders
    return render(request, template_name, data)

def order_claim(request, pk):
    print("order_claim")
    order = Order.objects.get(pk=pk)
    claimed = False
    if order:
        order.delete()
        claimed = True
    return HttpResponse(json.dumps({'claimed': claimed}), content_type='application/json')

@csrf_exempt
def order_create(request):
    try:
        order = json.loads(request.body)
        print('order_create: ', order)

        o = Order(description=order['description'],
                name=order['name'],
                office=order['office'],
                arrival_time = timezone.now())
        o.save()
        return HttpResponse(json.dumps({'id': o.pk}), content_type='application/json')
    except Exception as e:
        print('Exception: ', e)
    return HttpResponse(status=500)

def create_test(request):
    try:
        o = Order(description="description",
                name='name',
                office='office',
                arrival_time = timezone.now())
        o.save()
        return HttpResponse(json.dumps({'id': o.pk}), content_type='application/json')
    except Exception as e:
        print('Exception: ', e)
        return HttpResponse(status=500)

