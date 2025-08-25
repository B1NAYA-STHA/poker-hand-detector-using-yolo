from itertools import combinations

#function to return combination of cards
def all_hands(cards):
    #print(list(combinations(cards, 5)))
    return list(combinations(cards, 5))

if __name__ == "__main__":
    all_hands(["AH", "KH", "QH", "JH", "10H", "7H"])
    all_hands(["1H", "2D", "3H", "3D", "3C"])
    