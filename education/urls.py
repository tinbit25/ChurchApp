from django.urls import path
from .views import EducationalContentListCreateView

urlpatterns = [
    path('', EducationalContentListCreateView.as_view(), name='education-list'),
]
