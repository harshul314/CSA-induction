cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random


is_play = True

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
if play == 'n':
    is_play = False
while is_play:
    def deal_card():
        card = random.choice(cards)
        return card


    user_cards = []
    computer_cards = []

    for number in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    def calculate_score():
        global user_score
        global computer_score
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)

        if user_score == 21 or computer_score == 21:
            return 0
        elif user_score > 21 or computer_score > 21:
            cards[0] = 1


    calculate_score()

    print(f"Your cards : {user_cards},current  score: {user_score}\n")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score < 21 and computer_score < 21:

        global hit_or_stand
      
        hit_or_stand = input("Type 'y' to hit and 'n' to stand.")
        if hit_or_stand == 'y':
            user_cards.append(deal_card())
            calculate_score()

    if hit_or_stand == 'y':
        print(user_cards)
        print(f"Your current score : {user_score}")

    while computer_score < 17:
        computer_cards.append(deal_card())
        calculate_score()


    def compare(user_score, computer_score):
        if user_score == computer_score and user_score != 21:
            print("Draw")
        if calculate_score() == 0:
            if computer_score == 21:
                print("You loose")
            elif user_score == 21:
                print("You win!")
        elif user_score > 21 and computer_score < 21:
            print("Score over 21. You loose.")
        elif computer_score > 21 and user_score < 21:
            print("Computer looses")
        elif user_score < 21 and computer_score < 21:
            if user_score > computer_score:
                print("user wins.")
            elif computer_score > user_score:
                print("computer wins.")
        elif user_score > 21 and computer_score > 21:
            print("Draw.")


    print(f"user cards : {user_cards}, user score : {user_score}\n")
    print(f"computer cards : {computer_cards}, computer score : {computer_score}")

    compare(user_score, computer_score)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
    if play == 'n':
        is_play = False
