import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []

def black_jack():
    global is_game_on
    global is_continue

    is_game_on = True
    is_continue = True

    choice = input("Do you want to play BlackJack? Y or N: ").strip().lower()

    if choice == 'n':
        is_game_on = False
        return
    elif choice == 'y':
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))
        print(f"Player's first card: {player}")
        print(f"Dealer's first card: {dealer[0]}")  # show only one dealer card

        while is_continue:
            continue_game = input("Do you want to draw one more card (y or n)? ").strip().lower()
            if continue_game == "y":
                player.append(random.choice(cards))
                print(f"Player's cards: {player}")
                print(f"Current total: {sum(player)}")
                dealer.append(random.choice(cards))

                if sum(player) > 21:
                    print("You went over 21. You lose!")
                    break
            else:
                is_continue = False
                print("Game stopped.")
                print(f"Your final hand: {player} (Total: {sum(player)})")
                print(f"Dealer's hand: {dealer} (Total: {sum(dealer)})")
                if sum(dealer)>sum(player) and sum(dealer)<=21:
                    print("You have lost")
                elif sum(player)>sum(dealer) and sum(player)<=21:
                    print("You won")


    else:
        print("Please enter a valid input. (y or n)")
        black_jack()

black_jack()