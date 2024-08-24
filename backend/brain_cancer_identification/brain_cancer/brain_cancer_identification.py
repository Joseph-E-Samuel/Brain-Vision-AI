from tensorflow.keras.models import load_model
import cv2
import numpy as np

def predict_with_model(image_path):
    # Load the model
    model_path = '../../Brain-Tumor-Detection/models/cnn-parameters-improvement-10-0.85.keras'
    print(f"Loading model from {model_path}...")
    model = load_model(filepath='/Users/iniyan/workspace/Brain-Vision-AI/backend/brain_cancer_identification/brain_cancer/cnn-parameters-improvement-10-0.85.keras')
    print("Model loaded successfully.")

    # Function to prepare the image
    def prepare_image(image_path, target_size):
        print(f"Loading image from {image_path.name}...") 
        image = cv2.imread('/Users/iniyan/workspace/Brain-Vision-AI/backend/brain_cancer_identification/brain_cancer/Y10.jpg')
        
        if image is None:
            print(f"Error: Image at {image_path} could not be loaded.")
            return None
        
        print("Resizing image...")
        image = cv2.resize(image, target_size)
        
        print("Normalizing image...")
        image = image / 255.0
        
        print(f"Reshaping image to (1, {target_size[0]}, {target_size[1]}, 3)...")
        image = np.reshape(image, (1, target_size[0], target_size[1], 3))
        
        print("Image preparation complete.")
        return image

    # Define the target size (must match the size used during model training)
    IMG_WIDTH, IMG_HEIGHT = 240, 240
    # image_path = 'Y10.jpg'  # Replace with the path to your image

    # Prepare the image
    image = prepare_image(image_path, (IMG_WIDTH, IMG_HEIGHT))

    if image is not None:
        # Predict the class of the image
        print("Making prediction...")
        prediction = model.predict(image)
        
        print(f"Raw model output (probability): {prediction[0][0]}")
        
        # Convert probability to binary class
        predicted_class = np.where(prediction > 0.5, 1, 0)
        if(predicted_class[0][0]==1):
            return 'tumor detected'
        else:
            return 'no tumor detected'
    else:
        return("Image preparation failed; skipping prediction.")
