# Pomegranate Disease Detection using CNN
 - ## Introduction

    This project is a web-based application that leverages a Convolutional Neural Network (CNN) to identify common diseases in pomegranates. Users can upload an image of a pomegranate, and the machine learning model will analyze it to detect diseases such as Bacterial Blight, Bitter Rot, and Pomegranate Butterfly.

    The application provides a user-friendly interface for farmers and agricultural professionals to quickly diagnose potential issues with their crops and receive recommendations for treatment.

 - ## Features
    - Utilizes a trained Keras/TensorFlow model to accurately classify pomegranates into four categories:
        1. Bacterial Blight
        2. Bitter Rot
        3. Pomegranate Butterfly
        4. Healthy
    - It also displays suggested pesticides and fungicides based on the prediction.

- ## Technologies Used
    - Backend: Python, Flask
    - Machine Learning: TensorFlow, Keras, Scikit-learn
    - Image Processing: OpenCV, Pillow
    - Frontend: HTML, CSS, Bootstrap 5, JavaScript
    - Data Handling: NumPy, Matplotlib

- ## Setup and Installation
    - To get this project running on your local machine, follow these simple steps.
        1. Clone the Repository
            git clone https://github.com/your-username/Final-Year-Project.git
            
            cd Final-Year-Project

        2.  Create a Virtual Environment

            - For macOS/Linux

                python3 -m venv venv
                source venv/bin/activate

            - For Windows

                python -m venv venv
                venv\Scripts\activate

        3. Install Dependencies (If pip doesn't work try with pip3)

            pip install flask werkzeug opencv-python tensorflow keras numpy matplotlib pillow scikit-learn
        
        4. Run the Application (By starting Flask development server)

            python3 mySite.py
        
        5. View in Browser (Open the browser of your choice and navigate to:)

            http://127.0.0.1:5000/

- ## How to Use
    - Navigate to the "Detect Disease" Page: From the home page, click on the "Detect Disease" link.
    - Upload an Image: Click the "Choose Image to Upload" button and select a clear image of a pomegranate. The image will upload and appear on the page automatically.
    - Analyze the Image: Click the "Test" button to process the image with the CNN model.
    - View Results: The prediction will be displayed in the "Test Report" card, with treatment suggestions in the card  below.

- ## Project Structure
    Here is an overview of the key files and directories in the project      

:

    Final-Year-Project/ 
    ├── Dataset/                 # Contains the training and testing image data
    ├── Results/                 # Model performance charts (Accuracy, Loss, etc.)
    ├── static/
    │   ├── css/                 # Custom CSS stylesheets (style.css)
    │   └── images/              # Static images for the UI (backgrounds, etc.)
    ├── templates/
    │   ├── home.html            # The landing page
    │   ├── image.html           # The main page for uploading and testing
    │   ├── info.html            # About the project page
    │   └── layout.html          # The base HTML template with navigation and footer
    ├── upload/                  # Default directory for user-uploaded images
    ├── cnn_train.py             # Script to train the CNN model (if included)
    ├── mySite.py                # The main Flask application file
    ├── supportFile.py           # Helper script containing the prediction logic
    └── Trained_model.h5         # The pre-trained Keras model file

- ## Contributing
    Contributions are welcome! If you have suggestions for improvements, please feel free to fork the repository and submit a pull request.

- ## License
    This project is licensed under the MIT License.