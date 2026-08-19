# 🖐️ Hand Gesture & Computer Vision

A collection of real-time **Computer Vision projects** built using **Python, OpenCV, and MediaPipe**.

These projects explore hand landmark detection, finger counting, and gesture-based control, progressing from basic hand tracking to practical human-computer interaction.

---

## 🚀 Projects

### 1. 🖐️ Real-Time Hand Landmark & Index Finger Tracking

A foundational hand tracking project that detects up to two hands using MediaPipe and identifies all 21 landmarks on each hand.

The project also tracks the **index finger tip (landmark #8)** and displays its real-time pixel coordinates.

**Main concepts:**

* Hand landmark detection
* 21-point hand tracking
* Normalized coordinates
* Pixel coordinate conversion
* Index finger tracking

---

### 2. ☝️ Real-Time Hand Landmark & Finger Counter

An extension of hand landmark detection that uses landmark positions to determine how many fingers are raised.

The system supports up to two hands and calculates both individual and total finger counts.

**Main concepts:**

* Hand landmark detection
* Finger counting
* Landmark-based geometric logic
* Multi-hand detection
* Real-time webcam processing

Example:

```text
Hand 1: 5
Hand 2: 3
Total Fingers: 8
```

---

### 3. 💡 Real-Time Finger-Based Light Control

A gesture-based control project that converts the number of raised fingers into a brightness value.

```text
0 fingers →   0%
1 finger  →  20%
2 fingers →  40%
3 fingers →  60%
4 fingers →  80%
5 fingers → 100%
```

The finger count is converted into a value between **0 and 255**, making it suitable for future PWM-based hardware control.

**Main concepts:**

* Finger detection
* Gesture-based control
* Brightness mapping
* Computer Vision
* Human-Computer Interaction
* Future Arduino/PWM integration

---

## 🧠 Project Progression

The three projects demonstrate a progression from basic landmark detection to gesture-based control:

```text
🖐️ Hand Detection
       ↓
📍 21 Hand Landmarks
       ↓
☝️ Finger Detection
       ↓
🔢 Finger Counting
       ↓
💡 Brightness Control
       ↓
🤖 Future Hardware Integration
```

---

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **MediaPipe**
* **Computer Vision**

### Future Technologies

* Arduino
* PWM
* Serial Communication
* Embedded Systems

---

## 📊 Comparison

| Project                    | Main Function                 | Hands | Main Concept          |
| -------------------------- | ----------------------------- | ----: | --------------------- |
| 🖐️ Hand Landmark Tracking | Track hand landmarks          |     2 | Landmark Detection    |
| ☝️ Finger Counter          | Count raised fingers          |     2 | Gesture Analysis      |
| 💡 Light Control           | Convert fingers to brightness |     1 | Gesture-Based Control |

---

## 🔍 Common Workflow

All projects follow a similar computer vision pipeline:

```text
Webcam
   ↓
OpenCV Frame Capture
   ↓
BGR → RGB
   ↓
MediaPipe Hand Landmarker
   ↓
21 Hand Landmarks
   ↓
Computer Vision Logic
   ↓
Real-Time Output
```

---

## 💡 Applications

These projects can serve as building blocks for:

* 👋 Gesture recognition
* 🖱️ Virtual mouse control
* 🎮 Gesture-based interfaces
* 💡 Touchless lighting
* 🏠 Smart home control
* 🤖 Robotics
* 🦾 Embedded systems
* 🖥️ Human-Computer Interaction
* ✋ Sign language recognition

---

## 🔮 Future Improvements

Planned extensions include:

* ✋ Advanced gesture recognition
* 👍 Thumbs-up detection
* ✌️ Peace gesture detection
* 👊 Fist detection
* 👌 OK gesture detection
* 🖱️ Virtual mouse control
* 💡 Physical LED brightness control
* 🔌 Arduino integration
* 📡 Serial communication
* 🤖 Robotics control

---

## 🎯 Learning Objectives

Through these projects, I explored:

* Real-time computer vision
* MediaPipe Hand Landmarker
* Hand landmark coordinates
* Coordinate systems
* Finger detection logic
* Gesture-based interaction
* OpenCV webcam processing
* The connection between AI/CV and embedded systems
