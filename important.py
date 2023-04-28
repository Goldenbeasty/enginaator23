# Import the required modules
import flask
import os
import time
from google.cloud import vision
import io

# Create a flask app
app = flask.Flask(__name__)

# kui leiab drooni, siis tagastab True, kui ei leia, siis False
def detect_drone(path, side):
    """Detects labels in the file."""

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vast-torus-361119-74ecb27c5856.json"
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_label_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    # print('Labels:')

    for label in labels:
        if label.description == 'Aircraft' or label.description == 'Bird' or label.description == 'Air travel' or label.description == 'Aviation' or label.description == 'Person' or label.description == 'Car':
            detections_file = "/home/pi/.config/enginaator/detections.txt"
            if not os.path.exists(detections_file):
                with open(detections_file, "w") as tf:
                    tf.write()
                    tf.close()
            with open(detections_file, "a") as f:
                f.write(f"{side} {path}\n")
                f.close()
            return True
        # print(label.description)
        # print(label.confidence)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))





# Define a route for handling POST requests of jpeg images
@app.route('/north', methods=['POST'])
def north():
    # Get the request body as bytes
    print("<3 north")
    data = flask.request.get_data()
    # Check if the data is valid and has a jpeg header
    if True:
        # Create a directory for saving the images if it does not exist
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Generate a unique filename for the image
        filename = os.path.join(directory, 'north-' + str(int(time.time())) + '.jpeg')
        # Save the image to disk
        with open(filename, 'wb') as f:
            f.write(data)
        detect_drone(filename, side='north')
        # Return a success message
        return 'Image saved successfully'
    else:
        # Return an error message
        return 'Invalid data or format'

@app.route('/east', methods=['POST'])
def east():
    # Get the request body as bytes
    print("<3 east")
    data = flask.request.get_data()
    # Check if the data is valid and has a jpeg header
    if True:
        # Create a directory for saving the images if it does not exist
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Generate a unique filename for the image
        filename = os.path.join(directory, 'east-' + str(int(time.time())) + '.jpeg')
        # Save the image to disk
        with open(filename, 'wb') as f:
            f.write(data)
        detect_drone(filename, side='east')
        # Return a success message
        return 'Image saved successfully'
    else:
        # Return an error message
        return 'Invalid data or format'


@app.route('/south', methods=['POST'])
def south():
    # Get the request body as bytes
    print("<3 south")
    data = flask.request.get_data()
    # Check if the data is valid and has a jpeg header
    if True:
        # Create a directory for saving the images if it does not exist
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Generate a unique filename for the image
        filename = os.path.join(directory, 'south-' + str(int(time.time())) + '.jpeg')
        # Save the image to disk
        with open(filename, 'wb') as f:
            f.write(data)
        detect_drone(filename, side='south')
        # Return a success message
        return 'Image saved successfully'
    else:
        # Return an error message
        return 'Invalid data or format'


@app.route('/west', methods=['POST'])
def west():
    # Get the request body as bytes
    print("<3 west")
    data = flask.request.get_data()
    # Check if the data is valid and has a jpeg header
    if True:
        # Create a directory for saving the images if it does not exist
        directory = 'images'
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Generate a unique filename for the image
        filename = os.path.join(directory, 'west-' + str(int(time.time())) + '.jpeg')
        # Save the image to disk
        with open(filename, 'wb') as f:
            f.write(data)
        detect_drone(filename, side='west')
        # Return a success message
        return 'Image saved successfully'
    else:
        # Return an error message
        return 'Invalid data or format'


# Run the app on port 5000
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

