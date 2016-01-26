from django.conf.urls import url, include

from restaurants.urls import router

urlpatterns = [
    url(r'^', include(router.urls))
]
