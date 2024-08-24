
from django.urls import path
from .views import BrainCancerIdentificationAPIView

urlpatterns = [
    path('images/', BrainCancerIdentificationAPIView.as_view(), name='brain-cancer-identification-api-view'),
]