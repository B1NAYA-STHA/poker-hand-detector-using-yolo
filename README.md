🃏 Poker Hand Detection using YOLO
Real-time poker card recognition system using YOLO and OpenCV to detect cards from webcam feed and identify the best 5-card poker hand.

🧠 Features
🔍 Detects 52 standard playing cards using a trained YOLO model.

🧮 Identifies best possible 5-card poker hand from 7 cards (e.g., Texas Hold’em).

🎨 Highlights best-hand cards in a different color.

🖼 Displays labeled bounding boxes with confidence scores.

🧠 Modular code with customizable labeling and logic.

🛠️ Tech Stack
Ultralytics YOLO

Python + OpenCV

Custom trained YOLO model (playingCards.pt)

Real-time video processing (via webcam)

🚀 Getting Started
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/poker-hand-detection.git
cd poker-hand-detection
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

nginx
Copy
Edit
ultralytics
opencv-python
3. Run the App
bash
Copy
Edit
python detect.py
Make sure your webcam is enabled.
