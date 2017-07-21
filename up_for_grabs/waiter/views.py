# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from waiter.models import Order

import json
import django
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail

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

def send_email(subject, message, email_to):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)

def order_claim(request, pk):
    print("order_claim: " + str(pk))
    order = Order.objects.get(pk=pk)
    claimed = False
    name = ''
    description = ''
    restaurant = ''
    email = ''
    if order:
        name = order.name
        description = order.description
        restaurant = order.restaurant
        email = order.email
        order.delete()
        claimed = True
        send_email("Thank you!", "The food that you put up-for-grabs has been claimed!", email)
    return HttpResponse(json.dumps({'claimed': claimed, 'name': name, 'description': description, 'restaurant': restaurant, 'email': email}), content_type='application/json')

@csrf_exempt
def order_create(request):
    try:
        print request.body.decode('utf-8')
        order = json.loads(request.body.decode('utf-8'))
        print('order_create: ', order)

        o = Order(description=order['description'],
                name=order['name'],
                office=order['office'],
                email=order['email'],
                restaurant=order['restaurant'],
                arrival_time = timezone.now())
        o.save()
        return HttpResponse(json.dumps({'id': o.pk}), content_type='application/json')
    except Exception as e:
        print('Exception: ', e)
    return HttpResponse(status=500)

def create_test(request):
    try:
        print "create_test"
        o = Order(description="description",
                email='yahor.yuzefovich@cloudera.com',
                name='name',
                office='office',
                arrival_time = timezone.now())
        o.save()
        return HttpResponse(json.dumps({'id': o.pk}), content_type='application/json')
    except Exception as e:
        print('Exception: ', e)
        return HttpResponse(status=500)

