# donations/urls.py
from django.urls import path
from .views import DonationCreateView

urlpatterns = [
    path('', DonationCreateView.as_view(), name='donation-create'),  # This is fine
]
