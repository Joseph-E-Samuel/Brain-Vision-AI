from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BrainCancerIdentification
from django.http import JsonResponse, HttpResponseBadRequest
from .brain_cancer_identification import predict_with_model


class BrainCancerIdentificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = BrainCancerIdentification.objects.all()
        data = list(queryset.values())  # Convert queryset to list of dictionaries
        return JsonResponse(data, safe=False)

    def post(self, request):
        if "image" not in request.FILES:
            return HttpResponseBadRequest("No image file found in the request.")

        try:
            # Create new instance of MyModel using the data
            # Save the uploaded image
            image_file = request.FILES["image"]
            brain_cancer_identification = BrainCancerIdentification.objects.create(
                image=image_file
            )
            prediction_from_model = predict_with_model(image_path=image_file)
            brain_cancer_identification.prediction = prediction_from_model
            brain_cancer_identification.save()
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
