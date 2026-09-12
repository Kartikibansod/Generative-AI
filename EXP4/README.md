# 🎨 Experiment 4 — Text-to-Image Generation using Stable Diffusion XL

Generate AI-powered images from natural language prompts using a **pre-trained Stable Diffusion XL** model from Hugging Face Diffusers.

---

## 🌟 About

This experiment implements a **Text-to-Image Generation** system using a pre-trained diffusion model. The application converts user-provided text prompts into high-quality images and provides an interactive interface using **Gradio** for real-time image generation.

## 🎯 Aim

To implement a Generative AI image-generation system using a pre-trained diffusion model and generate images based on natural-language prompts.

## 🚀 Features

* Generate images from text prompts.
* Use the **Stable Diffusion XL (SDXL)** pre-trained model.
* Customize image generation using inference steps and guidance scale.
* Interactive web interface built with **Gradio**.
* GPU acceleration support for faster image generation in Google Colab.

## 🛠️ Tech Stack

| Technology             | Purpose                    |
| ---------------------- | -------------------------- |
| Python                 | Programming Language       |
| PyTorch                | Deep Learning Framework    |
| Hugging Face Diffusers | Stable Diffusion Pipeline  |
| Transformers           | Model Dependencies         |
| Accelerate             | Efficient GPU Execution    |
| Safetensors            | Model Loading              |
| Gradio                 | Interactive User Interface |
| Google Colab           | Development Environment    |

## ⚙️ How It Works

1. Load the pre-trained **Stable Diffusion XL** model.
2. Accept a natural-language prompt from the user.
3. Generate an image using the diffusion pipeline.
4. Display the generated image through a Gradio interface.
5. Experiment with different prompts and generation parameters to observe output variations.

## 📂 Repository Structure

```text
EXP4/
├── Text-to-Image.ipynb
├── generated_images/
├── README.md
```

## 💡 Sample Prompt

```text
A futuristic city at sunset with flying cars, cinematic lighting, ultra-realistic, 8K.
```

## 📸 Output

The notebook generates AI-created images based on user prompts. Different prompts and parameter values produce unique visual results using the same pre-trained diffusion model.

## 📖 Learning Outcomes

* Understand the basics of diffusion-based image generation.
* Learn prompt engineering for text-to-image models.
* Implement Stable Diffusion XL using Hugging Face Diffusers.
* Build an interactive image-generation application with Gradio.

## ✅ Conclusion

This experiment demonstrates how modern diffusion models transform natural-language descriptions into images. It provides hands-on experience with Stable Diffusion XL, prompt engineering, and interactive Generative AI applications.

