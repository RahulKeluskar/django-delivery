from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Restaurant, OpenHours, MenuItem


class OpenHoursSerializer(serializers.ModelSerializer):

    day_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = OpenHours
        fields = ('restaurant', 'links', 'day', 'day_display', 'from_hour', 'to_hour')
        
    def get_day_display(self, obj):
        return obj.get_day_display()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'restaurant': reverse(
                'restaurant-detail',
                kwargs={'pk':obj.restaurant.pk},
                request=request
            )
        }

class MenuItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.HyperlinkedRelatedField(view_name='restaurant-detail',
                                                     read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ('restaurant', 'name', 'description', 'price', 
            'availability', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self' : reverse('menuitem-detail',
                kwargs={'pk':obj.id}, request=request)
        }

class RestaurantSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'description', 'cuisine',
            'price', 'delivers', 'site_url', 'links')

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('restaurant-detail',
                kwargs={'pk':obj.id},request=request),
            'hours': None,
            'menu': None
        }

        if obj.open_hours: 
            links['hours'] = reverse('restaurant-hours',
                kwargs={'pk':obj.id}, request=request)

        if obj.menu_item:
            links['menu'] = reverse('restaurant-menu',
                kwargs={'pk':obj.id}, request=request)

        return links

        

