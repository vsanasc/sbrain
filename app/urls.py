
from django.urls import path, include

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]