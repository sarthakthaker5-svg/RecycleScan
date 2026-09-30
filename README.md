# ♻️ RecycleScan

### AI-Powered Waste Identification System

RecycleScan is an AI-powered waste identification application that uses **Deep Learning and Computer Vision** to identify different types of waste from images. The project uses **TensorFlow, Keras, and MobileNetV2** to classify waste into multiple categories and provides the prediction with confidence and recycling recommendations.

---

## 📌 Project Overview

Proper waste segregation is important for effective recycling and environmental protection. However, people may find it difficult to identify the correct category of waste.

**RecycleScan** provides a simple solution where users can upload an image of waste, and the AI model analyzes the image and predicts its waste category.

The application is developed using **Python and Streamlit** with a trained **MobileNetV2 transfer-learning model**.

---

## 🎯 Objectives

* ♻️ Identify different types of waste using AI.
* 🗑️ Help users understand proper waste categories.
* 🌱 Encourage better waste segregation and recycling.
* 🤖 Apply Deep Learning and Computer Vision to a real-world problem.
* 📱 Provide a simple and user-friendly interface.

---

## ✨ Features

* 📷 Upload a waste image.
* 🤖 AI-based waste classification.
* 📊 Displays prediction confidence.
* ♻️ Provides recycling recommendations.
* 🖥️ Simple and user-friendly Streamlit interface.
* 🚀 Can be accessed through a web browser.
* 📱 Mobile-friendly interface.

---

## 🗂️ Waste Categories

The model is trained to identify **10 different waste categories**:

1. Cardboard
2. E-Waste
3. Glass
4. Metal
5. Organic
6. Paper
7. Plastic
8. Shoes
9. Textile
10. Trash

---

## 🛠️ Technologies Used

| Technology  | Purpose                                 |
| ----------- | --------------------------------------- |
| Python      | Main programming language               |
| TensorFlow  | Deep Learning framework                 |
| Keras       | Building and loading the neural network |
| MobileNetV2 | Image classification model              |
| NumPy       | Image and numerical processing          |
| Streamlit   | Web application interface               |
| PIL         | Image loading and processing            |

---

## 🧠 Machine Learning Model

RecycleScan uses **MobileNetV2** with **Transfer Learning**.

MobileNetV2 is a lightweight Convolutional Neural Network (CNN) designed for image classification. Transfer learning allows the model to use knowledge learned from a large image dataset and adapt it to waste classification.

### Model Pipeline

```text
Waste Image
     ↓
Image Preprocessing
     ↓
MobileNetV2
     ↓
Feature Extraction
     ↓
Global Average Pooling
     ↓
Dropout
     ↓
Dense Layer
     ↓
Waste Category Prediction
     ↓
Confidence + Recommendation
```

---

## 📁 Project Structure

```text
RecycleScan/
│
├── app.py
├── recyclescan_balanced_model.keras
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sarthakthaker5-svg/RecycleScan.git
```

### 2. Open the Project Folder

```bash
cd RecycleScan
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

After running the command, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 🖼️ How to Use

1. Open the RecycleScan application.
2. Upload an image of waste.
3. The application processes the image.
4. The AI model predicts the waste category.
5. The prediction confidence is displayed.
6. A recycling recommendation is provided.

---

## 🌍 Social Significance

RecycleScan can help create awareness about proper waste segregation and responsible disposal. By making waste identification easier, the project aims to encourage people to separate waste correctly and support recycling practices.

---

## 🚀 Future Enhancements

* 📱 Develop a dedicated Android/iOS application.
* 📷 Add real-time camera-based waste detection.
* 🌐 Support more waste categories.
* 🔊 Add voice-based results.
* 🌍 Add multilingual support.
* 📍 Provide information about nearby recycling centers.
* 🤖 Improve model accuracy with a larger and more diverse dataset.
* 📊 Add waste detection statistics and history.

---

## 👨‍💻 Project Information

**Project Name:** RecycleScan
**Project Type:** AI / Machine Learning / Computer Vision
**Application:** Waste Identification and Classification
**Framework:** TensorFlow & Keras
**Web Framework:** Streamlit
**Model:** MobileNetV2

---

## 📜 License

This project is developed for **educational and academic purposes**.

---

## ⭐ Acknowledgement

This project was developed as part of an academic project to explore the practical application of **Artificial Intelligence, Deep Learning, Computer Vision, and Web Application Development** for environmental sustainability.

---

### ♻️ RecycleScan — Identify Waste. Sort Smart. Recycle Better.
