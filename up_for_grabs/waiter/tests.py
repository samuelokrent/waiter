# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

import json

# Create your tests here.

class OrderTestCase(TestCase):

    def get_orders(self, c):
        response = c.get('/testlist', content_type = 'application/json')
        return json.loads(response.content)

    def create_order(self, c, order, verbose=True):
        response = c.post('/create', json.dumps(order), content_type = 'application/json')
        self.assertEqual(200, response.status_code)
        if verbose:
            print('Content: ', json.loads(response.content))
        return json.loads(response.content)

    def claim_order(self, c, order_id, verbose=True):
        response = c.post('/claim/{}'.format(order_id), content_type = 'application/json')
        self.assertEqual(200, response.status_code)
        if verbose:
            print('Content: ', json.loads(response.content))
        return json.loads(response.content)

    def test_orders_can_be_created(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')

        orders = self.get_orders(c)
        print('orders 1: ', orders)
        self.assertEqual([], orders)

        order = {
            'description': 'burrito',
            'email': 'yahor.yuzefovich@cloudera.com',
            'name': 'yahor',
            'office': 'PA',
            'restaurant': 'In-N-Out'
        }
        self.create_order(c, order)
        
        orders = self.get_orders(c)
        print('orders 2: ', orders)
        order['id'] = orders[0]['id']
        self.assertEqual([order], orders)

    def test_orders_can_be_claimed(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')

        order = {
            'description': 'burrito',
            'email': 'yahor.yuzefovich@cloudera.com',
            'name': 'yahor',
            'office': 'PA',
            'restaurant': 'In-N-Out'
        }
        create_response = self.create_order(c, order)

        claim_response = self.claim_order(c, create_response['id'])

        self.assertTrue(claim_response['claimed'])

