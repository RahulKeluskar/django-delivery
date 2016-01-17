from django.shortcuts import render

from rest_framework import (authentication, 
    permissions, viewsets, filters, generics)

from .models import Restaurant, MenuItem, OpenHours
from .serializers import (RestaurantSerializer, MenuItemSerializer,
    OpenHoursSerializer)

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

class MenuViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating restaurants"""

    queryset = MenuItem.objects.order_by('name')
    serializer_class = MenuItemSerializer

class MenuList(generics.ListCreateAPIView):
    """API endpoint for listing and creating menus"""
    model = MenuItem
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            return MenuItem.objects.filter(restaurant=pk)
        return []

class OpenHoursList(generics.ListCreateAPIView):
    """API endpoint for listing and creating menus"""
    model = OpenHours
    serializer_class = OpenHoursSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            return OpenHours.objects.filter(restaurant=pk)
        return []
