from django.urls import path, include

from .views import WrapperView

from finance.modules.dashboard.factories import TableViewFactory

urlpatterns = [
    
    path(
        'api/table/<int:year>/<int:month>/<int:before>/<int:after>/',
        WrapperView.as_view(view_factory=TableViewFactory),
        name='dashboard'
    )

]