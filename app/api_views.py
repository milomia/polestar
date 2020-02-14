from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from app.serializers import ShipSerializer,PositionSerializer
from app.models import Ship,Position

class ShipList(ListAPIView):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

class PositionList(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends= (DjangoFilterBackend,)
    filter_fields = ('imo_number',)
