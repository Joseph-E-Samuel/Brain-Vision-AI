
from django.urls import path
from .views import BrainImageListCreateView

urlpatterns = [
    path('images/', BrainImageListCreateView.as_view(), name='brainimage-list-create'),
]