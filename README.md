# 🃏 Poker Hand Detection using YOLO

A real-time poker card recognition system using YOLO and OpenCV to detect cards from a webcam feed or a video and identify the best 5-card poker hand.

---

## 🧠 Features

- 🔍 Detects 52 standard playing cards using a custom trained YOLO model.
- 🧮 Identifies best 5-card poker hand from 7 cards.
- 🎯 Monte Carlo Simulation: Estimates your win probability against multiple opponents.
- 🎨 Color-Coded Display: Highlights the cards contributing to your best hand in green.
- 💬 Custom Label Renderer: Stylish label display for card name and confidence.
- 🔀 Separation Logic: Separates community and player cards based on position.
- 🧠 Modular code with customizable logic.

---

## 🛠️ Tech Stack

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- Python + OpenCV
- Trained YOLOv8 model (`playingCards.pt`)
- Real-time video streaming

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/poker-hand-detection.git
cd poker-hand-detection
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Run the Project

```bash
python detect.py
```
### Make sure your webcam is connected.

### 4. Optional: Run on a Video File

#### Uncomment and modify cap = cv.VideoCapture("path_to_video.mp4") in detect.py.
