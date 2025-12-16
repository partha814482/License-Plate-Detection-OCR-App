

# 🚘 License Plate Detection & OCR App

This project is an **end-to-end computer vision application** that detects a vehicle’s **license plate** from an uploaded image and extracts the **plate number using OCR (Optical Character Recognition)**.

It is built using **Streamlit**, **OpenCV**, and **Tesseract OCR**, and demonstrates a complete **image processing → detection → text extraction pipeline**.

---

## 🏗️ Project Architecture (Working Flow)

```
User Uploads Image (Streamlit UI)
        ↓
Image Preprocessing (OpenCV)
        ↓
Edge Detection (Canny)
        ↓
Contour Detection
        ↓
License Plate Localization
        ↓
Plate Cropping
        ↓
OCR using Tesseract
        ↓
Extracted Text Display
```

---

## 🧠 Core Technologies Used

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| Streamlit     | Web UI & interaction         |
| OpenCV        | Image processing & detection |
| Imutils       | Image resizing               |
| Tesseract OCR | Text extraction from images  |
| NumPy         | Image array processing       |
| PIL           | Image handling               |

---

## 📂 Code Architecture

### 1️⃣ User Interface (Streamlit)

```python
st.title("License Plate Detection & OCR App")
st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
```

✔ Allows user to upload images
✔ Displays intermediate results step-by-step

---

### 2️⃣ Image Loading & Conversion

```python
file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
```

✔ Converts uploaded image into OpenCV format
✔ Enables image processing operations

---

### 3️⃣ Image Preprocessing

#### 🔹 Grayscale Conversion

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

✔ Reduces color complexity
✔ Improves edge detection accuracy

---

#### 🔹 Noise Reduction (Bilateral Filter)

```python
smooth = cv2.bilateralFilter(gray_image, 11, 17, 17)
```

✔ Removes noise
✔ Preserves edges (important for plates)

---

### 4️⃣ Edge Detection

```python
edged = cv2.Canny(smooth, 30, 200)
```

✔ Detects sharp boundaries
✔ Highlights license plate edges

---

### 5️⃣ Contour Detection

```python
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```

✔ Finds all object boundaries
✔ Used to identify rectangular plate regions

---

### 6️⃣ Top Contours Filtering

```python
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
```

✔ Filters largest contours
✔ Improves detection accuracy

---

### 7️⃣ License Plate Detection Logic

```python
approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
if len(approx) == 4:
```

✔ Detects rectangular shapes
✔ License plates are usually rectangular
✔ First valid rectangle is selected

---

### 8️⃣ License Plate Cropping

```python
x, y, w, h = cv2.boundingRect(c)
detected_img = image[y:y+h, x:x+w]
```

✔ Crops detected plate region
✔ Prepares image for OCR

---

### 9️⃣ OCR (Text Extraction)

```python
text = pytesseract.image_to_string(detected_img)
```

✔ Extracts text from plate image
✔ Displays detected license number

---

## 🖥️ End-to-End Execution Flow

| Step | Action                           |
| ---- | -------------------------------- |
| 1    | User uploads image               |
| 2    | Image converted to OpenCV format |
| 3    | Grayscale & noise removal        |
| 4    | Edge detection                   |
| 5    | Contour detection                |
| 6    | Plate localization               |
| 7    | Plate cropped                    |
| 8    | OCR applied                      |
| 9    | Plate number displayed           |

---

## 🎯 Features

* ✅ Step-by-step image visualization
* ✅ Automatic license plate detection
* ✅ OCR-based text extraction
* ✅ Simple and interactive Streamlit UI
* ✅ Real-time results

---

## ⚙️ Requirements

```bash
pip install streamlit opencv-python imutils pytesseract pillow numpy
```

Also install **Tesseract OCR**:

* Windows: [https://github.com/UB-Mannheim/tesseract/wiki/Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki/Tesseract-OCR)

Update path in code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

---

## 📌 Limitations

* Works best with clear, frontal license plates
* Sensitive to lighting & image quality
* OCR accuracy depends on plate clarity

---

## 🔮 Future Enhancements

* 🚗 Support for video input
* 🌍 Country-specific plate formats
* 🧠 Deep learning–based detection (YOLO / SSD)
* 🧹 OCR post-processing & cleanup
----
## 🖥️ Application Screenshots
<img width="1913" height="866" alt="Screenshot 2025-12-16 214431" src="https://github.com/user-attachments/assets/268a84d2-ad27-4fe1-aa82-2bca4a7ee095" />

---

## 👨‍💻 Author

**Parthasarathi Behera**
Data Analyst | Computer Vision & AI Enthusiast

