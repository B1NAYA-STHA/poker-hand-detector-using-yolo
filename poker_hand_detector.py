from ultralytics import YOLO
import cv2 as cv
import math
import poker_hand_func
import label_func
from cards_names import classNames
import simulation
import save_video_func

cap = cv.VideoCapture(0)  # For Webcam
#cap = cv.VideoCapture("Poker_hand_detection_using_yolo\\resources\\video2.mp4")  # Video file
#output_video_url = "Poker_hand_detection_using_yolo\output_video\\1.mp4"
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO('Poker_hand_detection_using_yolo\playingCards.pt')

#video_write = save_video_func.video_writer(output_video_url, fps=30, frame_size=(1280, 720))

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
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
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
    
    #remove copies of cards
    hand = list(set(hand))
    player_cards = list(set(player_cards))
    community_cards = list(set(community_cards))

    # Only run simulation when player has 2 hole cards and at least 3 community cards
    if len(player_cards) == 2 and len(community_cards) >= 3:
        #simulate to get the probabilities
        estimated_prob = simulation.simulate(player_cards, community_cards)

        full_hand = player_cards + community_cards  # Combine both to form a 7-card hand

        if len(full_hand) >= 5:
            # Evaluate best possible hand from the available cards
            rank, best_hand, rank_score = poker_hand_func.findPokerHand(full_hand[:7])
            print(rank)        
            print(best_hand)   


        #display hand
        label_func.show_hand(frame, f'Your hand: {rank}, Your card: {best_hand}')
        label_func.show_hand(frame, f"Estimated Probability of winning: {estimated_prob:.4f}", start_pos=(10, line_y))

    #display line that seprates player and community card
    cv.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)

    #save_video_func.save_video(video_write, frame)

    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#video_write.release
cap.release()
cv.destroyAllWindows()

