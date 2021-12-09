import os

import io
from flask import Flask, request
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from flask_cors import cross_origin
import pandas as pd
import base64
from PIL import Image
app = Flask(__name__)


def preprocess_base64image(base64img):
    splitted_base64 = base64img.split(',')
    filtered_base64 = splitted_base64[1]
    base64_in_bytes = filtered_base64.encode('ascii')
    decoded_img = base64.b64decode(base64_in_bytes)
    img = Image.open(io.BytesIO(decoded_img))
    img = img.convert('RGB')
    return img


def preprocess_image_dimension(raw_img):
    img = raw_img.resize((150, 150))
    img = img_to_array(img)
    img = img.reshape(-1, 150, 150, 3)
    return img


@app.route("/check-green-scene", methods=["POST"])
@cross_origin()
def checkGreenScene():
    base64img = request.json['imageencoded']
    rawimg = preprocess_base64image(base64img)
    img = preprocess_image_dimension(rawimg)
    result = model.predict(img)
    return str(int(result[0][0]))


if __name__ == "__main__":
    model = load_model("./model_green_scene.h5")
    app.run(host="0.0.0.0", port="5000", debug=True)
