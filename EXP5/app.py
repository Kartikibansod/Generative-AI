from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import base64
import io
import os
from PIL import Image, ImageEnhance

app = Flask(__name__)

# -----------------------------
# Load Decoder
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "vae_mnist_models", "vae_decoder.keras")

decoder = tf.keras.models.load_model(MODEL_PATH)

print("✅ Decoder Loaded")

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Generate Digit
# -----------------------------
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        selected_digit = int(data["digit"])

        # Random latent vector
        latent_dim = decoder.input_shape[1]
        z = tf.random.normal((1, latent_dim))

        prediction = decoder.predict(z, verbose=0)[0]
        prediction = np.squeeze(prediction)

        prediction = np.clip(prediction, 0, 1)
        prediction = (prediction * 255).astype(np.uint8)

        image = Image.fromarray(prediction)

        # Resize without blur
        image = image.resize((336, 336), Image.Resampling.NEAREST)

        # Increase contrast
        image = ImageEnhance.Contrast(image).enhance(2.2)

        # Sharpen
        image = ImageEnhance.Sharpness(image).enhance(3)

        buffer = io.BytesIO()
        image.save(buffer, format="PNG")

        encoded = base64.b64encode(buffer.getvalue()).decode()

        return jsonify({
            "success": True,
            "selected_digit": selected_digit,
            "image": encoded
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)