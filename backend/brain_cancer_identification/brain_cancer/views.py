from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BrainCancerIdentification
from django.http import JsonResponse

class BrainCancerIdentificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = BrainCancerIdentification.objects.all()
        data = list(queryset.values())  # Convert queryset to list of dictionaries
        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            # Create new instance of MyModel using the data
            instance = BrainCancerIdentification.objects.create(**data)
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
