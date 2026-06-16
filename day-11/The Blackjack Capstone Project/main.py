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









# import random
# from art import logo


# def deal_card():
#     """Returns a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card


# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0

#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)

#     return sum(cards)


# def compare(u_score, c_score):
#     """Compares the user score u_score against the computer score c_score."""
#     if u_score == c_score:
#         return "Draw 🙃"
#     elif c_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif u_score == 0:
#         return "Win with a Blackjack 😎"
#     elif u_score > 21:
#         return "You went over. You lose 😭"
#     elif c_score > 21:
#         return "Opponent went over. You win 😁"
#     elif u_score > c_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"


# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     computer_score = -1
#     user_score = -1
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()
