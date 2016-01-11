from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Restaurant, OpenHours

#A good explanation of how to set up the hours with a serializer
#http://stackoverflow.com/questions/25202222/django-rest-framework-setting-up-serializer-for-foreign-key


class HoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenHours
        fields = ('from_hour', 'to_hour',
            'day')

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