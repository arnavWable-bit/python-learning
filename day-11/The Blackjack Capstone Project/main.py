import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards) :
    total_sum = sum(cards)
    while 11 in cards and total_sum > 21:
        cards.remove(11)
        cards.append(1)
        total_sum = sum(cards)

    return total_sum


should_continue = True
while should_continue:

    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print("\n" *20)
    if want_to_play == 'n':
        should_continue = False

    else :
        print(logo)
        user_card = [deal_card(), deal_card()]
        total_sum = calculate_score(user_card)
        print(f"Your cards: {user_card}, current score: {total_sum}")

        computer_card = [deal_card(),deal_card()]
        computer_total = calculate_score(computer_card)
        print(f"Computer's first card: {computer_card[0]}")

        if total_sum == 21 and computer_total != 21:
            print("You win!")
            player_turn = False
        elif total_sum != 21 and computer_total == 21:
            print("You lose!")
            player_turn = False
        elif total_sum == 21 and computer_total == 21 :
            print("Draw!")
            player_turn = False
        else:
            player_turn = True

        
        while player_turn:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'n':
                player_turn = False
            else :
                user_card.append(deal_card())
                total_sum= calculate_score(user_card)
                print(f"Your cards: {user_card}, current score: {total_sum}")
                print(f"Computer's first card: {computer_card[0]}")

                if total_sum > 21:
                    player_turn = False
                    
                    print(f"Your final hand: {user_card}, final score: {total_sum}")
                    print(f"Computer's final hand: {computer_card}, final score: {computer_total}")

                    print("You went over. You lose")

                

        if total_sum <= 21:
            computer_total = calculate_score(computer_card)
            while computer_total < 17:
                computer_card.append(deal_card())
                computer_total = calculate_score(computer_card)

            print(f"Your final hand: {user_card}, final score: {total_sum}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_total}")

            if computer_total > 21:
                print("You Win!")
                
            elif total_sum > computer_total:
                print("You win!")

            elif total_sum < computer_total:
                print("You lose!")
            else:
                print("Draw!")
