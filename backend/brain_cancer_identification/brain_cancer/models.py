from django.db import models

class BrainCancerIdentification(models.Model):
    image = models.ImageField(upload_to='brain_images/')  # Stores the image file
    prediction = models.BooleanField(null=True)  # Stores the prediction as a boolean (True/False)

    def __str__(self):
        return f"Image {self.id} - Prediction: {'Positive' if self.prediction else 'Negative'}"
