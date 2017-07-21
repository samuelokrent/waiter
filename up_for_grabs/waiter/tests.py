# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

import json

# Create your tests here.

class OrderTestCase(TestCase):

    def get_orders(self, c):
        response = c.get('/testlist', content_type = 'application/json')
        return json.loads(response.content)

    def test_orders_can_be_created(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')

        orders = self.get_orders(c)
        print('orders 1: ', orders)
        self.assertEqual([], orders)

        order = {
            'description': 'burrito',
            'name': 'yahor',
            'office': 'PA'
        }
        response = c.post('/create', json.dumps(order), content_type = 'application/json')
        print('Content: ', response.content)
        self.assertEqual(200, response.status_code)

        orders = self.get_orders(c)
        print('orders 2: ', orders)
        self.assertEqual([order], orders)
