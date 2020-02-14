from rest_framework.test import APITestCase

import rest_framework
from app.utils import load_position_data
import datetime

from django.test import TestCase
from django.utils import timezone

from django.test import TestCase

from app.models import Position

# Create your tests here.

class PositionTests(TestCase):
 
  def test_data_loaded(self):
    load_position_data('/users/milomia/Desktop/positions.csv')
    count = Position.objects.count()
    icount=int(count)
    self.assertEqual(icount , 2000)

'''
class PositionListTestCase(APITestCase):
    def test_list_positions(self):
        #load_position_data('/users/milomia/Desktop/positions.csv')
        breakpoint()
        positions_count = Position.objects.count()
        breakpoint()
        response = self.client.get('/api/positions/')
        breakpoint()
        icount=int(response.data['count'])
        self.assertEqual(icount, positions_count)
        self.assertEqual(len(response.data['results']), positions_count)
'''


