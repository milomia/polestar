from rest_framework import serializers

from app.models import Ship,Position


class ShipSerializer(serializers.ModelSerializer):
   class Meta:
      model=Ship
      fields = ('name','imo_number')

   def to_representation(self,instance):
       data = super().to_representation(instance)
       return data

class PositionSerializer(serializers.ModelSerializer):
   class Meta:
      model=Position
      fields = ('id', 'imo_number', 'timestamp','latitude','longitude')

   def to_representation(self,instance):
       data = super().to_representation(instance)
       return data
