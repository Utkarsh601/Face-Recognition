# Face Recognition App 👀

This is a simple **Face Recognition App** built with **Python**, **OpenCV**, and **Streamlit**. The application uses Haarcascade classifiers to detect faces and eyes from an image or webcam feed.

## Features
- Face Detection using Haarcascade Classifier.
- Eye Detection using Haarcascade Classifier.
- Real-time video feed processing.
- Easy-to-use web interface built with **Streamlit**.
- Deployed on **Streamlit Cloud (share.streamlit.io)**.

## Demo
[Face Recognition App](https://face-recognition-project.streamlit.app/)

## Technologies Used
- **Python** - Programming language used for building the app.
- **OpenCV** - Library for image processing and computer vision tasks.
- **Streamlit** - Framework for creating web interfaces quickly and easily.

## Setup Instructions

### Prerequisites
- Python 3.10 or less
- pip (Python package installer)

### Installation
1. Clone the repository:
```bash
    git clone https://github.com/Utkarsh601/Face-Recognition.git
```
2. Navigate to the project directory:
```bash
    cd face-recognition-app
```
3. Install the required packages:
```bash
    pip install -r requirements.txt
```

### Running the App Locally
```bash
    streamlit run app.py
```

## Project Structure
```
face-recognition-app/
│
├── app.py               # Streamlit app script
├── requirements.txt     # Dependencies list
│── haarcascade_frontalface_default.xml
│── haarcascade_eye.xml
└── README.md            # Project README file
```

## Usage
- Upload an image or use your webcam to detect faces and eyes.
- The application highlights detected faces and eyes in real-time.

## Deployment
The app is deployed on Streamlit Cloud and can be accessed [here](https://face-recognition-project.streamlit.app/).

