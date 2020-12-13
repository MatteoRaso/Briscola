#!/usr/bin/python
#When two players play their card, this function is called to determine who wins.
#player_1 is the one that plays first.
#The reason that we have a 'best' attribute is because whoever has the best card
#gets to draw and play first for the next card.
def better_card(card_1, card_2, player_1, player_2, briscola):

    total_points = card_1.points + card_2.points

    player_1.best = False
    player_2.best = False

    if card_1.suit == briscola and card_2.suit == briscola:
        if card_1.points > card_2.points:
            player_1.points += total_points
            player_1.best = True

        else:
            player_2.points += total_points
            player_2.best = True

    elif card_1.suit != card_2.suit:
        player_1.points += total_points
        player_1.best = True

    elif card_1.points > card_2.points:
        player_1.points += total_points
        player_1.best = True

    else:
        player_2.points += total_points
        player_2.best = True

    return player_1, player_2
