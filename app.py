import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance
import cv2 as cv2



faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes=cv2.CascadeClassifier('haarcascade_eye.xml')

def detect_faces(up_image):
	detect_img=np.array(up_image.convert('RGB'))
	new_img1=cv2.cvtColor(detect_img,1)
	faces=faceDetect.detectMultiScale(new_img1,1.3,5)
	for x,y,w,h in faces:
		cv2.rectangle(new_img1,(x,y),(x+w,y+h),(0,128,255),2)
	return new_img1,faces

def detect_eye(up_image):
	detect_img=np.array(up_image.convert('RGB'))
	new_img1=cv2.cvtColor(detect_img,1)
	faces=eyes.detectMultiScale(new_img1,1.3,5)
	for x,y,w,h in faces:
		cv2.rectangle(new_img1,(x,y),(x+w,y+h),(0,128,255),2)
	return new_img1,faces



def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        h1, h2, h3 {
            color: #0A66C2;
        }
        .stButton > button {
            background-color: #0A66C2;
            color: white;
            border-radius: 8px;
        }
        .stButton > button:hover {
            background-color: #0A66C2;
            opacity: 0.8;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Face Detection App for CyFuture")
    st.write("Built with Streamlit and OpenCV")
    activites=["Detection", "About"]
    choices=st.sidebar.selectbox("Select Activities", activites)

    if choices=="Detection":
        st.subheader("Face Detection")
        img_file=st.file_uploader("Upload File",type=['png','jpg','jpeg'])
        if img_file is not None:
            up_image=Image.open(img_file)
            st.image(up_image)

        enhance_type=st.sidebar.radio("Enhance type", ["Original","Gray-scale","Contrast","Brightness","Blurring"])

        if enhance_type=="Gray-scale":
            new_img=np.array(up_image.convert('RGB'))
            gray=cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            st.image(gray)

        if enhance_type=="Contrast":
            c_make=st.sidebar.slider("Contrast", 0.5, 3.5)
            enhancer=ImageEnhance.Contrast(up_image)
            img_out=enhancer.enhance(c_make)
            st.image(img_out)

        if enhance_type=="Brightness":
            b_make=st.sidebar.slider("Brightness", 0.5, 3.5)
            enhancer=ImageEnhance.Brightness(up_image)
            img_bg=enhancer.enhance(b_make)
            st.image(img_bg)

        if enhance_type=="Blurring":
            br_make=st.sidebar.slider("Blurring", 0.5, 3.5)
            br_img=np.array(up_image.convert('RGB'))
            b_img=cv2.cvtColor(br_img, 1)
            blur=cv2.GaussianBlur(b_img,(11,11),br_make)
            st.image(blur)

        task=["Faces", "Eyes"]
        feature_choice=st.sidebar.selectbox("Find Feature", task)

        if st.button("Process"):
            if feature_choice=="Faces":
                result_img, result_faces=detect_faces(up_image)
                st.image(result_img)
                st.success("Found {} faces".format(len(result_faces)))

            if feature_choice=="Eyes":
                result_img, result_faces=detect_eye(up_image)
                st.image(result_img)
                st.success("Found {} Eyes".format(len(result_faces)))

    elif choices=="About":
        st.write("This Application is Developed by Utkarsh Mishra")


if __name__=='__main__':
    main()
