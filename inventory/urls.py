from django.urls import (include, path)
from rest_framework.routers import DefaultRouter

from inventory import views

router = DefaultRouter()

router.register('strains', views.StrainsView)

urlpatterns = [
        path('', include(router.urls)),
        ]
