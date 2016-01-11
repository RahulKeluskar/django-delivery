from django.shortcuts import render

from rest_framework import (authentication, 
    permissions, viewsets, filters)

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer

class DefaultsMixin(object):
    """Default setings for view authentication, pagination, 
    permissions, and filtering."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )

    permission_classes = (
        permissions.IsAuthenticated,
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

class MenuViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating menus"""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    