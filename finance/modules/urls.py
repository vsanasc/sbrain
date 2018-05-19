from django.urls import re_path, include

from .dashboard import urls as DashboardUrls

urlpatterns = [
    
    re_path(
        r'finance/dashboard/',
        include(DashboardUrls),
        name='dashboard'
    )

]