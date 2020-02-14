from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path

import app.views
import app.api_views

urlpatterns = [
    path('api/ships/', app.api_views.ShipList.as_view()),
    path('api/positions/', app.api_views.PositionList.as_view()),
    path('admin/', admin.site.urls),
]
