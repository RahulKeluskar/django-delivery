from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menu-items', views.MenuViewSet)
urlpatterns = router.urls

urlpatterns.extend([
    url(r'^restaurants/(?P<pk>\d+)/hours/$',
        views.OpenHoursList.as_view(),
        name='restaurant-hours'),
    url(r'^restaurants/(?P<pk>\d+)/menu/$',
        views.MenuList.as_view(),
        name='restaurant-menu')
])