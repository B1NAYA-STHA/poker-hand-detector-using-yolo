import list_of_hand_func

def findPokerHand(cards):
    best_hand = None
    best_hand_score = (0, [])  # (hand_rank, kicker list)
    pokerHandRanks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four of a Kind", 7: "Full House", 6: "Flush",
                      5: "Straight", 4: "Three of a Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
    
    all_hand_list = list_of_hand_func.all_hands(cards)
    for hand in all_hand_list:
        ranks = []
        suits = []
        possibleRanks = []
        #get the ranks and suits from each card
        for card in hand:
            if len(card) == 2:
                rank = card[0]
                suit = card[1]
            else:
                rank = card[0:2]
                suit = card[2]
            
            if rank == "A": rank = 14
            elif rank == "K": rank = 13
            elif rank == "Q": rank = 12
            elif rank == "J": rank = 11
            ranks.append(int(rank))
            suits.append(suit)
        
        #sort the ranks of the cards
        sortedRank = sorted(ranks)

        #check for royal flush, straight flush and flush
        if (suits.count(suits[0]) == 5):
            if sortedRank == [10, 11, 12, 13, 14]:
                possibleRanks.append(10)
            elif all(sortedRank[i] == sortedRank[i-1] + 1 for i in range(1, len(sortedRank))):
                possibleRanks.append(9)
            else:
                possibleRanks.append(6)
        
        #check for straight
        if all(sortedRank[i] == sortedRank[i-1] + 1 for i in range(1, len(sortedRank))):
            possibleRanks.append(5)
        
        #get a set for unique values in the rank
        uniqueHandVals = set(sortedRank)

        #check for four of a kind and full house
        if len(uniqueHandVals) == 2:
            for val in uniqueHandVals:
                if sortedRank.count(val) == 4:  #four of a kind
                    possibleRanks.append(8)
                elif sortedRank.count(val) == 3:  #full house
                    possibleRanks.append(7)

        #check for three of a kind and two pair
        elif len(uniqueHandVals) == 3:
            for val in uniqueHandVals:
                if sortedRank.count(val) == 3: #three of a kind
                    possibleRanks.append(4)
                elif sortedRank.count(val) == 2: #two pair
                        possibleRanks.append(3)
        
        elif len(uniqueHandVals) == 4:
            possibleRanks.append(2)

        if not possibleRanks:
            possibleRanks.append(1)
        
        current_rank = max(possibleRanks)  # Highest hand type for this 5-card hand

        current_kickers = sorted(sortedRank, reverse=True)  # For tie-breaking

        current_score = (current_rank, current_kickers)

        if current_score > best_hand_score:  # Compare hand strength
            best_hand_score = current_score
            best_hand = hand

    output = pokerHandRanks[best_hand_score[0]]  # Get hand name
    return output, best_hand


if __name__ == "__main__":
    #findPokerHand(["AH", "KH", "QH", "JH", "10H", "7H", "AC"])  # Royal Flush
    #findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    #findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    #findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    #findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    #findPokerHand(["JC", "10H", "9C", "8C", "7D", "AC", "2C"])  # Straight
    #findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    #findPokerHand(["7D", "7H", "KC", "7S", "AD", "5D", "10H"])  # Two Pair
    #findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card