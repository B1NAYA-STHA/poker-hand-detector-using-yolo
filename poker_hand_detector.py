from ultralytics import YOLO
import cv2 as cv
import math
import poker_hand_func
import label_func

cap = cv.VideoCapture(0)  # For Webcam
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO('Poker_hand_detection_using_yolo\playingCards.pt')
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
    frame_height = frame.shape[0]
    line_y = int(frame_height * 0.6)
    hand = []
    player_cards = []
    community_cards = []
    for r in result:
        boxes = r.boxes
        for box in boxes:
            #bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            #confidence
            conf = math.ceil((box.conf[0] * 100)) / 100

            cls = int(box.cls[0])

            card_label = classNames[cls]

            #seprate player and community card based on physical position
            if y1 > line_y:
                player_cards.append(card_label)
            else:
                community_cards.append(card_label)

            # Choose color based on whether the card is in best_hand
            if 'best_hand' in locals() and card_label in best_hand:
                box_color = (0, 255, 0)  # Green for best hand cards
            else:
                box_color = (0, 0, 255)  # Red for others

            #Display the card
            cv.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
            label_func.draw_label(frame, f'{card_label}: {conf}', x1, y1, box_color)

            if conf > 0.3:
                hand.append(card_label)
    
    hand = list(set(hand))

    if len(player_cards) == 2 and len(community_cards) >= 3:
        full_hand = player_cards + community_cards
        if len(full_hand) >= 5:
            rank, best_hand = poker_hand_func.findPokerHand(full_hand[:7])
            print(rank)
            print(best_hand)

        #display hand
        label_func.show_hand(frame, f'Your hand: {rank}, Your card: {best_hand}')

    #display line that seprates player and community card
    cv.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)
    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

