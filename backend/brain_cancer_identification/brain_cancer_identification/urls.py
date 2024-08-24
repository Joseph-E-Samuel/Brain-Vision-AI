from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('brain_cancer.urls')),  # Include your app's URLs
]
