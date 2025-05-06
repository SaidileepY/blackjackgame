import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    # Handle Ace as 1 if total is over 21
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def black_jack():
    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]

    print(f"Your cards: {player}, current score: {calculate_score(player)}")
    print(f"Dealer's first card: {dealer[0]}")

    game_over = False

    while not game_over:
        choice = input("Type 'y' to draw another card, 'n' to pass: ").strip().lower()
        if choice == 'y':
            player.append(random.choice(cards))
            print(f"Your cards: {player}, current score: {calculate_score(player)}")
            if calculate_score(player) > 21:
                print("You went over 21. You lose!")
                return
        else:
            game_over = True

    # Dealer draws until score >= 17
    while calculate_score(dealer) < 17:
        dealer.append(random.choice(cards))

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    print(f"\nYour final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")

    # Result logic
    if player_score > 21:
        print("You lose.")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose.")
    else:
        print("It's a draw.")

# Game entry point
while True:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if start == 'y':
        black_jack()
    else:
        print("Goodbye!")
        break
