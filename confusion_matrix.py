import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os

# --- Configuration ---
MODEL_PATH = 'Trained_model.h5'
TEST_DATA_DIR = 'Dataset/test_set'
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
OUTPUT_PATH = 'Results/Confusion_Matrix.png'

# Define the correct class labels for your project
class_labels = ['Bacterial Blight-samples', 'Bitter Rot-samples', 'Butterfly Pomegranate-samples', 'Normal-samples (1)']

# --- 1. Load the Model ---
print("Loading the trained model...")
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
print("Model loaded successfully.")

# --- 2. Prepare the Test Data ---
print("Preparing the test data generator...")
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    TEST_DATA_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False  # IMPORTANT: Do not shuffle to keep labels in order
)
print(f"Found {test_generator.n} images belonging to {test_generator.num_classes} classes.")


# --- 3. Make Predictions ---
print("Making predictions on the test set...")
predictions = model.predict(test_generator, steps=test_generator.n // test_generator.batch_size + 1)
predicted_classes = np.argmax(predictions, axis=1)

# Get the true labels
true_classes = test_generator.classes

# --- 4. Generate and Save the Confusion Matrix ---
print("Generating the confusion matrix...")
cm = confusion_matrix(true_classes, predicted_classes)

# Use Scikit-learn's display for a nice plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_labels)

fig, ax = plt.subplots(figsize=(10, 10))
disp.plot(ax=ax, cmap=plt.cm.Blues, xticks_rotation='vertical')

plt.title('Confusion Matrix for Pomegranate Disease Detection')
plt.tight_layout() # Adjust layout to make room for labels

# Ensure the Results directory exists
if not os.path.exists('Results'):
    os.makedirs('Results')

plt.savefig(OUTPUT_PATH)

print(f"\nSuccess! The correct confusion matrix has been saved to: {OUTPUT_PATH}")

# --- 5. (Optional) Show the plot ---
plt.show()