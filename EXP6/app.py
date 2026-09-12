from flask import Flask, render_template
import torch
from torchvision.utils import save_image
import os

# Create Flask app
app = Flask(__name__)

# Device (CPU is fine for Mac)
device = "cpu"

# Absolute path to this project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to generator.pt
MODEL_PATH = os.path.join(BASE_DIR, "generator.pt")

# Load the trained DCGAN model
generator = torch.jit.load(MODEL_PATH, map_location=device)
generator.eval()

# Create static folder if it doesn't exist
STATIC_DIR = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html", generated=False)


@app.route("/generate")
def generate():
    # Random noise vector
    noise = torch.randn(1, 100, 1, 1).to(device)

    # Generate face
    with torch.no_grad():
        fake_image = generator(noise)

    # Convert output from [-1,1] to [0,1]
    fake_image = (fake_image + 1) / 2

    # Save generated image
    image_path = os.path.join(STATIC_DIR, "generated.png")
    save_image(fake_image, image_path)

    return render_template("index.html", generated=True)


if __name__ == "__main__":
    print("🚀 Starting DCGAN Face Generator...")
    app.run(host="127.0.0.1", port=5050, debug=True)