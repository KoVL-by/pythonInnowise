from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from support.models import Ticket, Category
from rest_framework import routers

from support.views import UserViewSet, TicketViewSet, CategoryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('api/users', UserViewSet)

router.register('api/tickets', TicketViewSet)

router.register('api/category', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))

]
