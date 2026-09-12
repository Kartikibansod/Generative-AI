# 👤 Experiment 6 — Face Generation using DCGAN on the CelebA Dataset

Generate realistic human face images using a **Deep Convolutional Generative Adversarial Network (DCGAN)** trained on the **CelebA** dataset with **PyTorch**.

---

## 🌟 About

This project implements a **Deep Convolutional Generative Adversarial Network (DCGAN)** to generate synthetic human face images. The model is trained on the **CelebA** dataset, where the **Generator** learns to create realistic faces while the **Discriminator** learns to distinguish between real and generated images. The project also includes a **Flask web application** for generating new faces interactively.

## 🎯 Aim

To implement a DCGAN using PyTorch, train it on the CelebA dataset, and generate realistic human face images using the trained Generator model.

## ✨ Key Features

* Train a DCGAN on the CelebA face dataset.
* Implement Generator and Discriminator using convolutional neural networks.
* Generate realistic face images from random latent noise vectors.
* Visualize generated images during training.
* Save and reuse the trained Generator model.
* Generate faces through a simple Flask web interface.

## 🛠️ Tech Stack

| Technology   | Purpose                           |
| ------------ | --------------------------------- |
| Python       | Programming Language              |
| PyTorch      | DCGAN implementation and training |
| Torchvision  | Image preprocessing and datasets  |
| NumPy        | Numerical computations            |
| Matplotlib   | Training and image visualization  |
| Flask        | Web application backend           |
| HTML/CSS     | User interface                    |
| Google Colab | Model training environment        |

## 🧩 DCGAN Architecture

The model consists of two neural networks trained simultaneously:

* **Generator** – Converts a 100-dimensional random noise vector into a **64×64 RGB face image** using transposed convolution layers.
* **Discriminator** – Classifies input images as **real** or **fake** using convolution layers and adversarial learning.

## ⚙️ Project Workflow

1. Load and preprocess the CelebA dataset.
2. Resize and normalize face images.
3. Build the Generator and Discriminator networks.
4. Train the DCGAN using Binary Cross-Entropy (BCE) Loss and the Adam optimizer.
5. Track Generator and Discriminator losses during training.
6. Save the trained Generator model.
7. Generate new face images from random latent vectors.
8. Launch the Flask application for interactive face generation.

## 📂 Repository Structure

```text id="fyy5zt"
EXP6/
├── app.py                 # Flask application
├── generator.pt           # Trained Generator model
├── static/                # Generated images and static assets
├── templates/             # HTML templates
├── Experiment6.ipynb      # Google Colab notebook
└── README.md
```

## ▶️ Running the Project

### 1. Install Dependencies

```bash id="mwtuj5"
pip install torch torchvision flask numpy matplotlib pillow
```

### 2. Run the Flask Application

```bash id="8vqeev"
python app.py
```

### 3. Open the Web Interface

After running the Flask server, open the local URL displayed in the terminal (typically `http://127.0.0.1:5000`) and click **Generate Face** to create a new AI-generated face.

## 📸 Results

The trained Generator creates realistic human face images by sampling random latent vectors from a normal distribution. Each generated image is unique and does not exist in the original CelebA dataset.

## 📖 Learning Outcomes

After completing this experiment, you will be able to:

* Understand the working principle of Generative Adversarial Networks.
* Implement the DCGAN architecture using PyTorch.
* Train Generator and Discriminator networks using adversarial learning.
* Generate synthetic face images from random noise vectors.
* Deploy a trained GAN model using Flask.

## ✅ Conclusion

This experiment demonstrates how DCGANs learn to generate realistic human faces through adversarial training. It provides practical experience with PyTorch, convolutional GAN architectures, latent space sampling, and deployment of a Generative AI model through a Flask web application.
