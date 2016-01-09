from django.shortcuts import render

from rest_framework import (authentication, 
    permissions, viewsets, filters)

from .models import Restaurant
from .serializers import RestaurantSerializer

class DefaultsMixin(object):
    """Default setings for view authentication, pagination, 
    permissions, and filtering."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )

class RestaurantViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating restaurants"""

    queryset = Restaurant.objects.order_by('name')
    serializer_class = RestaurantSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )