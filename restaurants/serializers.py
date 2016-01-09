from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('name', 'address', 'description', 'cuisine',
            'price', 'delivers', 'site_url', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self' : reverse('restaurant-detail',
                kwargs={'pk':obj.name},request=request)
        }
