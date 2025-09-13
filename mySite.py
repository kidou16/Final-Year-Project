# import the necessary packages
from flask import Flask, render_template, redirect, url_for, request,session,Response
from werkzeug.utils import secure_filename
from supportFile import predict
import os
import cv2

app = Flask(__name__)

app.secret_key = '1234'
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def landing():
	return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
	return render_template('info.html')



@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        savepath = r'upload/'
        if not os.path.exists(savepath):
            os.makedirs(savepath)

        # Check if the 'Test' button was clicked
        if 'sub' in request.form and request.form['sub'] == 'Test':
            result, pesticide, pesticide1, pesticide2 = predict()
            return render_template('image.html', result=result, pesticide=pesticide, pesticide1=pesticide1, pesticide2=pesticide2)
        
        # Check if a file was uploaded (for the automatic submission)
        elif 'photo' in request.files and request.files['photo'].filename != '':
            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            destination = os.path.join(savepath, filename)
            photo.save(destination)
            
            image = cv2.imread(destination)
            cv2.imwrite(os.path.join("static/images/", "test_image.jpg"), image)
            # Add a success message for the user
            return render_template('image.html', result="Image uploaded successfully! Click 'Test' to analyze.")

        # Handle case where form is submitted without a file (e.g., empty submit)
        else:
            return render_template('image.html', result="Please select an image to upload.")

    return render_template('image.html')

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	return response


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, threaded=True)
