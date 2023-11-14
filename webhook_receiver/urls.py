from django.urls import path
from .views import NotificationAPIView

urlpatterns = [
    path('notification/', NotificationAPIView.as_view(), name='notification'),
]