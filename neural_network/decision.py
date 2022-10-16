#The function that the output of the network will get
#pumped to. This function will decide which card is played.

def decision(output_nodes, hand, briscola):
    values = [output_nodes[0].value, output_nodes[1].value,
              output_nodes[2].value, output_nodes[3].value]

    if max(values) == output_nodes[0].value:
        action = 0

    elif max(values) == output_nodes[1].value:
        action = 1

    elif max(values) == output_nodes[2].value:
        action = 2

    else:
        action = 3

    #Network may have chosen an illegal action, so we need
    #to change the action to one that doesn't cause problems.
    if action == 0:
        if (hand[0].suit != briscola and hand[1].suit != briscola and hand[2].suit != briscola):
            action = 2

        else:
            possible_hands = []
            for card in hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[0]

    if action == 1:
        if (hand[0].suit != briscola and hand[1].suit != briscola and hand[2].suit != briscola):
            action = 2

        else:
            possible_hands = []
            for card in hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[1]

    if action == 2:
        if (hand[0].suit == briscola and hand[1].suit == briscola and hand[2].suit == briscola):
            action = 0

        else:
            possible_hands = []
            for card in hand:
                if card.suit != briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[0]

    if action == 3:
        if (hand[0].suit == briscola and hand[1].suit == briscola and hand[2].suit == briscola):
            action = 0

        else:
            possible_hands = []
            for card in hand:
                if card.suit != briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[1]

    if action == 0:
        possible_hands = []
        for card in hand:
            if card.suit == briscola:
                possible_hands.append(card)

        possible_hands.sort(key = lambda x: x.points, reverse = True)
        played_card = possible_hands[0]

    return played_card
