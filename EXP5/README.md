# 🧠 Experiment 5 — Variational Autoencoder (VAE) for MNIST Image Generation

A Generative AI project that implements a **Variational Autoencoder (VAE)** using **TensorFlow/Keras** to learn the latent representation of handwritten digits from the MNIST dataset and generate new MNIST-like images.

---

## 🌟 About

This experiment demonstrates how a **Variational Autoencoder (VAE)** can learn a compressed probabilistic representation of images and generate entirely new handwritten digits by sampling from the learned latent space. The project also includes a simple **Flask web application** for generating images using the trained decoder model.

## 🎯 Aim

To implement a Variational Autoencoder (VAE) using TensorFlow/Keras, train it on the MNIST handwritten digit dataset, and generate new MNIST-like images using the learned latent space and trained decoder.

## ✨ Key Features

* Train a Variational Autoencoder on the MNIST dataset.
* Learn a **2-dimensional latent space** representation of handwritten digits.
* Implement the **Reparameterization Trick** for latent vector sampling.
* Visualize reconstructed images and latent space embeddings.
* Generate new handwritten digits from random latent vectors.
* Save and reuse trained encoder and decoder models.
* Deploy the trained decoder through a simple Flask interface.

## 🛠️ Tech Stack

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Programming Language          |
| TensorFlow / Keras | Building and training the VAE |
| NumPy              | Numerical computations        |
| Matplotlib         | Visualization of results      |
| Flask              | Web application backend       |
| HTML/CSS           | Frontend interface            |
| Google Colab       | Model training environment    |

## 🧩 VAE Architecture

The implemented Variational Autoencoder consists of three main components:

* **Encoder** – Converts a 28×28 MNIST image into latent parameters (`z_mean` and `z_log_var`).
* **Latent Space** – Samples latent vectors using the Reparameterization Trick.
* **Decoder** – Reconstructs or generates new handwritten digit images from latent vectors.

## ⚙️ Project Workflow

1. Load and preprocess the MNIST dataset.
2. Normalize image pixel values.
3. Build the Encoder and Decoder networks.
4. Implement latent space sampling using the Reparameterization Trick.
5. Train the VAE using Reconstruction Loss and KL Divergence.
6. Visualize training loss and latent space distribution.
7. Generate reconstructed and new handwritten digit images.
8. Save the trained encoder and decoder models.
9. Run the Flask application for interactive image generation.

## 📂 Repository Structure

```text
EXP5/
├── app.py                  # Flask application
├── index.html              # Web interface
├── templates/              # HTML templates
├── vae_mnist_models/       # Saved encoder and decoder models
├── vae_mnist_models.zip    # Archived trained models
├── Experiment5.ipynb       # Google Colab notebook
└── README.md
```

## ▶️ Running the Project

### 1. Install Dependencies

```bash
pip install tensorflow flask numpy matplotlib
```

### 2. Start the Flask Application

```bash
python app.py
```

### 3. Open the Application

Visit the local server displayed in the terminal (usually `http://127.0.0.1:5000`) to generate new MNIST-like handwritten digits using the trained decoder.

## 📊 Results

The project demonstrates:

* Reconstruction of original MNIST images.
* Visualization of a 2D latent space.
* Generation of new handwritten digits from randomly sampled latent vectors.
* Interactive image generation through a Flask interface.

## 📖 Learning Outcomes

After completing this experiment, you will be able to:

* Understand the working principle of a Variational Autoencoder.
* Implement latent space sampling using the Reparameterization Trick.
* Train a VAE using TensorFlow/Keras.
* Generate new images from a learned latent distribution.
* Deploy a trained Generative AI model using Flask.

## ✅ Conclusion

This experiment provides hands-on experience with Variational Autoencoders and latent space learning for image generation. It demonstrates how probabilistic generative models can create new data samples and forms a strong foundation for more advanced Generative AI models such as GANs and diffusion models.
