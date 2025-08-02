# 🃏 Poker Hand Detection using YOLO

A real-time poker card recognition system using YOLO and OpenCV to detect cards from a webcam feed and identify the best 5-card poker hand.

---

## 🧠 Features

- 🔍 Detects 52 standard playing cards using a trained YOLO model.
- 🧮 Identifies best 5-card poker hand from 7 cards.
- 🎨 Highlights best-hand cards in a different color.
- 🖼 Displays labeled bounding boxes with confidence scores.
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
