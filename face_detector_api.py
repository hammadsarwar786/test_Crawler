from flask import Flask, request, jsonify
import base64
from PIL import Image
import io
import face_recognition
import numpy as np
import glob
import os

app = Flask(__name__)

#http://127.0.0.1:5000/detect_face

#request for API is: 
# {
# "imageToDetect": "base64-image-string"
# }

#To run the updated code, you need to install the following packages:

#Flask: pip install flask
#face_recognition: pip install face_recognition
#PIL (Python Imaging Library): pip install pillow
#You can install these packages using the pip package manager. Make sure you have a compatible version of Python installed on your system.

# List of image file paths to compare against
image_list = []

def preprocess_image(image_data):
    encoded = image_data.split(",", 1)[1]
    image_bytes = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return image

def find_matching_image(image_data):
    image_to_detect = preprocess_image(image_data)
    face_to_detect = face_recognition.face_encodings(np.array(image_to_detect))[0]

    for image_path in image_list:
        if image_path.lower().endswith(('.jpg', '.jpeg')):
            face_image = face_recognition.load_image_file(image_path)
            face_encodings = face_recognition.face_encodings(face_image)
            if len(face_encodings) > 0:
                match = face_recognition.compare_faces([face_to_detect], face_encodings[0])
                if match[0]:
                    return image_path

    return None

@app.route('/detect_face', methods=['POST'])
def detect_face():
    if 'imageToDetect' not in request.json:
        return jsonify({'error': 'No imageToDetect parameter provided'}), 400

    image_to_detect = request.json['imageToDetect']
    matched_image = find_matching_image(image_to_detect)

    if matched_image:
        return jsonify({'matchedImage': matched_image}), 200
    else:
        return jsonify({'message': 'Image not found'}), 404

if __name__ == '__main__':
    # Populate image_list with image file paths from the folder
    image_folder_path = "./images"
    image_list = [file for file in glob.glob(f"{image_folder_path}/*.jpg") if os.path.isfile(file)] + [file for file in glob.glob(f"{image_folder_path}/*.jpeg") if os.path.isfile(file)]

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
