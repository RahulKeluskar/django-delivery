from django.shortcuts import render

from rest_framework import authentication, permissions, viewsets

from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating restaurants"""

    queryset = Restaurant.objects.order_by('name')
    serializer_class = RestaurantSerializer

class DefaultsMixin(object):
    """Default setings for view authentication, pagination, 
    permissions, and filtering."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )