from cards_names import classNames
import poker_hand_func
import random

# Remove known cards from the deck (e.g., player's and community cards)
def remove_cards(cards, className):
    for card in cards:
        if card in className:
            className.remove(card)
    return className

# Monte Carlo simulation to estimate probability of winning
def simulate(player_card, comm_card, opponents=3, iterations=1000):
    wins = 0
    ties = 0

    for _ in range(iterations):
        # Create a temporary deck and remove known cards
        temp_classNames = classNames.copy()
        temp_classNames = remove_cards(player_card, temp_classNames)
        temp_classNames = remove_cards(comm_card, temp_classNames)

        all_opp_score = []

        # Generate hands for all opponents and evaluate their best scores
        for _ in range(opponents):
            new_player_card = random.sample(temp_classNames, 2)
            temp_classNames = remove_cards(new_player_card, temp_classNames)
            _, _, opp_score = poker_hand_func.findPokerHand(new_player_card + comm_card)
            all_opp_score.append(opp_score)

        # Evaluate your own hand score
        _, _, my_score = poker_hand_func.findPokerHand(player_card + comm_card)

        # Compare your score against all opponents
        if my_score > max(all_opp_score):
            wins += 1
        elif my_score == max(all_opp_score):
            ties += 1

    # Calculate estimated winning probability
    estimated_prob = wins / iterations

    print(f"Estimated Probability of winning: {estimated_prob:.4f}")
    return estimated_prob

# Example usage
if __name__ == "__main__":
    simulate(['10C', '5S'], ['10S', '9C', 'AS', '2S', '3S'])
