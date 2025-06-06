# ✋🤟 Hand Sign Language Detection - Real-Time ASL Interpreter

A real-time hand sign language detection system built using **OpenCV**, **Flask**, and **Deep Learning**. The system captures live webcam feed, detects hand gestures using the `cvzone` HandTrackingModule, and classifies the detected signs using a custom-trained **Keras model**.

---

## 📸 Project Demo  

### 🔵 Real-Time Hand Sign Detection  

<img src="https://github.com/user-attachments/assets/f1c49d65-c580-40db-b7a5-ed6cb97cea21" width="400"/>

---

### 🔤 ASL Signs Reference  

<img src="https://github.com/user-attachments/assets/d946abec-ecc8-4141-84ab-13ba6f944fd9" width="400"/>

---

## 📂 Features  

✅ Real-time hand sign detection using webcam  
✅ Pre-trained **Keras model** for ASL alphabet classification  
✅ Live web interface using **Flask**  
✅ Bounding box and label display on detected hand signs  
✅ Supports both single-hand detection and classification  

---

## 📚 Labels (Classes Taught to the Model)

| Label         | Description             |
|:--------------|:------------------------|
| A-Z            | American Sign Language alphabets |
| Calm Down     | Gesture for "Calm Down"  |
| Hello         | Gesture for "Hello"      |
| Love          | Gesture for "Love"       |
| Stand         | Gesture for "Stand"      |
| Thumbs Up     | Gesture for "Thumbs Up"  |
| Where         | Gesture for "Where"      |

---

---

## 🚀 How to Run  

### 1️⃣ Install Dependencies  

First, install all the required Python libraries:


---

### 2️⃣ Run the Application  

Once dependencies are installed, run the Flask application:


---

### 3️⃣ Open in Browser  

After running, open your browser and go to:
http://127.0.0.1:5000/


You should now see your webcam feed and real-time hand sign detection with labels.

---

## 🧠 Tech Stack  

- **Python 3**
- **Flask**
- **OpenCV**
- **cvzone**
- **TensorFlow / Keras**

---

## 📦 Requirements  

- A working **Webcam**
- Python libraries listed in `requirements.txt`
- Trained Keras model (`keras_model.h5`) and label file (`labels.txt`)

---

## 🎯 Future Improvements  

- Add multi-hand detection support  
- Extend gesture classes with more dynamic hand signs  
- Deploy the system on cloud platforms (Heroku, Render, or AWS) for public access  
- Improve UI for web interface  
- Implement multi-language support  

---

## 📃 License  

This project is for educational, personal, and research purposes only.

---

## 🙌 Acknowledgements  

- **cvzone** by Murtaza Hassan  
- **TensorFlow / Keras** community  
- American Sign Language (ASL) community and references  

