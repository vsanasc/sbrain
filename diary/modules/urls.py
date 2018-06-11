from django.urls import path, include

from diary.modules.resume.factories import (
    DateViewFactory
)

from .views import WrapperView

urlpatterns = [
    
    path(
        'api-diary/date/<int:year>/<int:month>/<int:day>/',
        WrapperView.as_view(view_factory=DateViewFactory),
        name='diary-date'
    )

]
