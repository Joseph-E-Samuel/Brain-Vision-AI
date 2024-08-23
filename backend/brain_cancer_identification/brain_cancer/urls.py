from django.urls import path
from .views import BrainCancerIdentificationAPIView

urlpatterns = [
    path('api/BrainCancerIdentification/', MyModelAPIView.as_view(), name='BrainCancerIdentification-api'),
]
