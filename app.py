import streamlit as st
import cv2
import numpy as np
import imutils
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("License Plate Detection & OCR App")
st.write("Upload an image to detect the license plate and extract text")

# File uploader
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.subheader("Original Image")
    st.image(image, channels="BGR")

    # Resize
    resized_image = imutils.resize(image)

    # Gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    st.subheader("Grayscale Image")
    st.image(gray_image, channels="GRAY")

    # Smooth
    smooth = cv2.bilateralFilter(gray_image, 11, 17, 17)

    st.subheader("Smoothened Image")
    st.image(smooth, channels="GRAY")

    # Edge detection
    edged = cv2.Canny(smooth, 30, 200)
    st.subheader("Edge Detection")
    st.image(edged, channels="GRAY")

    # Contours
    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()
    cv2.drawContours(image1, cnts, -1, (0, 255, 0), 2)

    st.subheader("All Contours")
    st.image(image1, channels="BGR")

    # Top 30
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    image2 = image.copy()
    cv2.drawContours(image2, cnts, -1, (0, 255, 0), 2)

    st.subheader("Top 30 Contours")
    st.image(image2, channels="BGR")

    # Detect plate
    screenCnt = None
    detected_img = None
    i = 7

    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            screenCnt = approx
            x, y, w, h = cv2.boundingRect(c)
            detected_img = image[y:y+h, x:x+w]
            break

    if screenCnt is not None:
        final = image.copy()
        cv2.drawContours(final, [screenCnt], -1, (0, 255, 0), 3)

        st.subheader("Detected License Plate")
        st.image(detected_img, channels="BGR")

        st.subheader("Image with Plate Marked")
        st.image(final, channels="BGR")

        # OCR
        text = pytesseract.image_to_string(detected_img)

        st.subheader("OCR Result")
        st.success(text)

    else:
        st.error("No license plate detected!")
