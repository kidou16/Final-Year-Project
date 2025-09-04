Pomegranate Disease Classification
This project is a final-year submission that utilizes a Convolutional Neural Network (CNN) to classify diseases in pomegranate leaves. The system is designed to identify four distinct classes: 'Bacterial Blight', 'Bitter Rot', 'Butterfly Pomegranate', and 'Normal'.

The project is structured into two main components:

Model Training: A Python script to train the CNN model on a pre-existing dataset.

Web Application: A user-friendly web interface built with Flask that allows users to upload an image of a pomegranate leaf and receive a real-time prediction of its condition.

Project Structure
The repository is organized as follows:

.
├── Dataset/
│   ├── test_set/             # Images for testing the trained model
│   └── training_set/         # Images for training the model
├── Results/
│   ├── Accuracy.png          # Plot of training/validation accuracy
│   └── Loss.png              # Plot of training/validation loss
├── static/
│   ├── css/                  # CSS files for styling the web application
│   └── images/               # Images used by the web application
├── templates/                # HTML files for the web application
├── upload/                   # Directory where uploaded images are temporarily stored
├── cnn_train.py              # Python script for training the CNN model
├── mySite.py                 # Main Python script for the Flask web application
├── supportFile.py            # Helper functions for the project
├── Trained_model.h5          # The pre-trained Keras model
└── README.md                 # This file


Getting Started
To get this project up and running locally, follow these steps.

Prerequisites
You need Python 3.0 installed on your system. You will also need the following Python libraries:

TensorFlow / Keras

Flask

NumPy

OpenCV (cv2)

Installation
Navigate to the project directory in your terminal.

It is highly recommended to use a virtual environment. You can create and activate one with the following commands:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS / Linux
source venv/bin/activate


Install the required dependencies. Since there is no requirements.txt file, you can install the main packages directly:

pip install tensorflow flask numpy opencv-python


Usage
1. Training the Model
The script cnn_train.py is used to train the Convolutional Neural Network. If you wish to retrain the model on the provided dataset, you can run this file. The script will save the trained model as Trained_model.h5 and keras_model.h5 and will also generate the performance plots in the Results/ directory.

python cnn_train.py


Note: A pre-trained model is already included in the project, so this step is optional if you only want to use the web application.

2. Running the Web Application
To start the web application, simply run the main site script:

python mySite.py


The application will start a local server. You can access it by opening your web browser and navigating to http://127.0.0.1:5000. From there, you can upload an image and see the model's prediction.

Results
The Results/ folder contains several plots that demonstrate the performance of the trained CNN model:

Accuracy.png: This plot shows the training and validation accuracy over each epoch, giving an insight into how well the model learned and generalized.

Loss.png: This plot shows the training and validation loss, which helps in identifying if the model is overfitting or underfitting.

Acknowledgments
This project was developed as a final-year project By Yugal Jagtap
