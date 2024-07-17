# NIfTI Image Similarity Metrics

![GitHub stars](https://img.shields.io/github/stars/vijay-kapse/volume-error-checker?style=social)
![GitHub forks](https://img.shields.io/github/forks/vijay-kapse/volume-error-checker?style=social)
![GitHub issues](https://img.shields.io/github/issues/vijay-kapse/volume-error-checker)
![GitHub license](https://img.shields.io/github/license/vijay-kapse/volume-error-checker)

## Overview

Welcome to the **NIfTI Image Similarity Metrics** repository! This project is a user-friendly web app built with Streamlit that allows you to upload two NIfTI images, calculate important similarity metrics, and visualize their overlap in 3D.

### Key Features

- **Metrics Calculation**: Computes the Dice coefficient, Jaccard index, Volume Overlap Error (VOE), and Coverage.
- **3D Visualization**: Visualizes the overlap between two NIfTI images using interactive 3D plots.
- **Easy-to-Use Interface**: Simple and intuitive web interface for uploading images and viewing results.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- Streamlit
- Nibabel
- NumPy
- Plotly

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/vijay-kapse/volume-error-checker.git
cd volume-error-checker
```


### Install the required packages:
```bash
pip install -r requirements.txt
```

### Running the App
Start the Streamlit app by running:
```bash
streamlit run app.py
```

This will launch the web app in your default web browser.

### Usage
- Upload NIfTI Images: Use the file uploaders to select your label and predicted label NIfTI images.
- Calculate Metrics: The app will automatically calculate the Dice coefficient, Jaccard index, VOE, and Coverage. 
- Visualize Overlap: Choose from different views (Label, Predicted Label, Intersection, Difference, All) to see the 3D overlap visualization.

### Example

![Screenshot 2024-07-17 103326](https://github.com/user-attachments/assets/6a1f4217-5126-4e57-a966-a95c66dc93e0)


### Acknowledgements
Inspired by the need for efficient and accurate image similarity metrics in medical imaging. - Built with love using Streamlit and Plotly.
