from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BrainCancerIdentification
from django.http import JsonResponse, HttpResponseBadRequest
from .brain_cancer_identification import predict_with_model


class BrainCancerIdentificationAPIView(APIView):

    def post(self, request):
        print(request)
        print('inside')
        if "image" not in request.FILES:
            print('error')
            return HttpResponseBadRequest("No image file found in the request.")
 

        # Create new instance of MyModel using the data
        # Save the uploaded image
        print('insdie')

        image_file = request.FILES["image"]

        # brain_cancer_identification = BrainCancerIdentification.objects.create(
        #     image=image_file
        # )
        print('IMAGEFILE: ', image_file)

        prediction_from_model = predict_with_model(image_path=image_file)
        print('PREDICTION: ', prediction_from_model)

        # brain_cancer_identification.prediction = prediction_from_model
        # brain_cancer_identification.save()
        return JsonResponse(prediction_from_model, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     print('error: ', e)
        #     return JsonResponse({"error": e}, status=status.HTTP_400_BAD_REQUEST)
