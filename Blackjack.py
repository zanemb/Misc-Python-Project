#       Write a program so it simulates a simplified version of the game of
#       Blackjack between two virtual players. The cards have the following 
#       values: Numeric cards are assigned the value they have printed on them.
#       For example, the value of the 2 of spades is 2, and the value of the 5
#       of diamonds is 5. Jacks, queens, and kings are valued at 10. Aces are
#       valued at 1 or 11, depending on the player’s choice.

#       The program should deal cards to each player until one player’s hand is
#       worth more than 21 points. When that happens, the other player is the
#       winner. (It is possible that both players’ hands will simultaneously
#       exceed 21 points, in which case neither player wins.) The program should
#       repeat until all the cards have been dealt from the deck.

#       If a player is dealt an ace, the program should decide the value of the
#       card according to the following rule: The ace will be worth 11 points,
#       unless that makes the player’s hand exceed 21 points. In that case, the
#       ace will be worth 1 point.

#       You should have a function to shuffle the deck before starting and after
#       playing through all of the cards.

deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3, '4 of Spades':4,
        '5 of Spades':5, '6 of Spades':6, '7 of Spades':7, '8 of Spades':8,
        '9 of Spades':9, '10 of Spades':10, 'Jack of Spades':10,
        'Queen of Spades':10, 'King of Spades': 10, 'Ace of Hearts':1,
        '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4, '5 of Hearts':5,
        '6 of Hearts':6, '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
        '10 of Hearts':10, 'Jack of Hearts':10, 'Queen of Hearts':10,
        'King of Hearts': 10, 'Ace of Clubs':1, '2 of Clubs':2,
        '3 of Clubs':3, '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
        '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9, '10 of Clubs':10,
        'Jack of Clubs':10, 'Queen of Clubs':10, 'King of Clubs': 10,
        'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
        '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
        '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
        '10 of Diamonds':10, 'Jack of Diamonds':10, 'Queen of Diamonds':10,
        'King of Diamonds': 10
        }

import random

def main():
    # create empty lists to split dictionary components into
    p1_cards, p1_vals, p2_cards, p2_vals = [], [], [], []
    # create variables to keep track of game stats
    game_nums, p1_wins, p2_wins, ties = 0, 0, 0, 0
    # loop to continue dealing while deck still has cards in it
    while len(deck) > 0:
        p1_cards, p1_vals = new_round(p1_cards, p1_vals, 1)
        p2_cards, p2_vals = new_round(p2_cards, p2_vals, 2)
        outcome = who_wins(p1_vals, p2_vals)
        if outcome == "tie":
            print("Players tied")
            ties += 1
            game_nums += 1
        elif outcome == "p1":
            print("Player 1 wins!")
            p1_wins += 1
            game_nums += 1
        elif outcome == "p2":
            print("Player 2 wins!")
            p2_wins += 1
            game_nums += 1
        else:
            continue
        # clear hands for next game
        p1_cards.clear()
        p1_vals.clear()
        p2_cards.clear()
        p2_vals.clear()
    display_report(game_nums, p1_wins, p2_wins, ties)

# function to split key from value in deck dictionary and add to separate lists
# shuffles deck keys before choosing one at random
def deal_one(cards, vals):
    list_deck = list(deck)
    # does shuffle functionally do anything if we are using choice right after?
    random.shuffle(list_deck)
    card = random.choice(list_deck)
    cards.append(card)
    vals.append(deck[card])
    remove_card = deck.pop(card)
    return cards, vals

# function to make iterating deals easier
def new_round(cards, vals, pnum):
    cards, vals = deal_one(cards, vals)
    display_hand(cards, vals, pnum)
    return cards, vals

# function to sum values in a list and make aces high or low
def sum_values(card_list):
    sum = 0
    for val in card_list:
        sum += val
    if 1 in card_list and sum < 21:
        sum += 10
    else: pass
    if 1 in card_list and sum > 21:
        sum -= 10
    else: pass
    return sum

# function to retrieve point total and display card name and point total
def display_hand(cards, vals, pnum):
    hand_total = sum_values(vals)
    print(f"Player {pnum} was dealt a(n) {cards[-1]}")
    print(f"Player {pnum}'s total is {hand_total}")
    return hand_total

# function to evaluate player totals and return game outcome
def who_wins(vals1, vals2):
    total1 = sum_values(vals1)
    total2 = sum_values(vals2)
    if total1 > 21 and total2 > 21:
        return "tie"
    elif total1 <= 21 and total2 > 21:
        return "p1"
    elif total1 > 21 and total2 <= 21:
        return "p2"
    else:
        return "it doesn't really matter what I put here"

# function to display end stats
def display_report(game_nums, p1_wins, p2_wins, ties):
    print("\nThe deck has run out of cards\n")
    print("Summary of games between Player 1 and Player 2:")
    print(f"Players played {game_nums} rounds of Blackjack")
    print(f"Player 1 won {p1_wins} game(s)")
    print(f"Player 2 won {p2_wins} game(s)")
    print(f"Players tied {ties} game(s)")

# call main function
main()

