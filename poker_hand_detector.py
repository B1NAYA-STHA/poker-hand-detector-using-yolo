from ultralytics import YOLO
import cv2 as cv
import math
import poker_hand_func

cap = cv.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO('YOLO\Poker_hand\playingCards.pt')
classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']

while True:
    ret, frame = cap.read()
    result = model(frame, stream=True)
    hand = []
    for r in result:
        boxes = r.boxes
        for box in boxes:
            #bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            #confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            cls = int(box.cls[0])

            #Display the card
            cv.rectangle(frame, (x1, y1), (x2,y2), (0, 255, 0), 2)
            cv.putText(frame, f'{classNames[cls]}: {conf}', (max(0, x1), max(40, y1)), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv.LINE_4)

            if conf > 0.3:
                hand.append(classNames[cls])
    
    hand = list(set(hand))
    print(hand)
    if len(hand) == 5:
        results = poker_hand_func.findPokerHand(hand)
        print(results)
        cv.putText(frame, f'Your hand: {results}', (400, 75), cv.FONT_HERSHEY_PLAIN, 3, (246, 70, 190), 3, cv.LINE_4)

    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

