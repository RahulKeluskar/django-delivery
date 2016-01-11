from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Restaurant, OpenHours, MenuItem

#A good explanation of how to set up the hours with a serializer
#http://stackoverflow.com/questions/25202222/django-rest-framework-setting-up-serializer-for-foreign-key


class HoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenHours
        fields = ('from_hour', 'to_hour',
            'day')

class MenuItemSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ('restaurant', 'name', 'description', 'price', 
            'availability', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self' : reverse('menuitem-detail',
                kwargs={'pk':obj.title}, request=request)
        }

class RestaurantSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
    hours = HoursSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'description', 'cuisine',
            'price', 'delivers', 'site_url', 'links', 'hours')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self' : reverse('restaurant-detail',
                kwargs={'pk':obj.name},request=request)
        }
    
    def create(self, validated_data):
        restaurant = Restaurant.objects.create(**validated_data)

        return restaurant

