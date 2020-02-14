from django.contrib.auth import get_user_model
from django.db import transaction
from csv import DictReader
import datetime
import uuid
import csv
import json

from datetime import datetime
from pytz import UTC
from .models import Position

def flush_position_data():
    """Flush data."""
    data = Position.objects
    data.all().delete()

def load_position_data(filename):

    flush_position_data()
    position = Position()

    arr = []
    headers = []

    csvfile = open(filename,"r")

    for row in csv.reader(csvfile):
        position = Position()
        position.imo_number=row[0]
        position.timestamp=row[1]
        position.latitude=row[2]
        position.longitude=row[3]
        position.save()

