#The function that the output of the network will get
#pumped to. This function will decide which card is played.

def decision(output_nodes, hand, briscola, first):
    if first:
        values = [output_nodes[0].value_1, output_nodes[1].value_1,
                  output_nodes[2].value_1, output_nodes[3].value_1]

        if max(values) == output_nodes[0].value_1:
            action = 0

        elif max(values) == output_nodes[1].value_1:
            action = 1

        elif max(values) == output_nodes[2].value_1:
            action = 2

        else:
            action = 3

    else:
        values = [output_nodes[0].value_2, output_nodes[1].value_2,
                  output_nodes[2].value_2, output_nodes[3].value_2]

        if max(values) == output_nodes[0].value_2:
            action = 0

        elif max(values) == output_nodes[1].value_2:
            action = 1

        elif max(values) == output_nodes[2].value_2:
            action = 2

        else:
            action = 3

    if len(hand) >= 3:
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
                played_card = possible_hands[-1]

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
                played_card = possible_hands[-1]

        if action == 0:
            possible_hands = []
            for card in hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[0]

    elif len(hand) == 2:
        if action == 0:
            if (hand[0].suit != briscola and hand[1].suit != briscola):
                action = 2

            else:
                possible_hands = []
                for card in hand:
                    if card.suit == briscola:
                        possible_hands.append(card)

                possible_hands.sort(key = lambda x: x.points, reverse = True)
                played_card = possible_hands[0]

        if action == 1:
            if (hand[0].suit != briscola and hand[1].suit != briscola):
                action = 2

            else:
                possible_hands = []
                for card in hand:
                    if card.suit == briscola:
                        possible_hands.append(card)

                possible_hands.sort(key = lambda x: x.points, reverse = True)
                played_card = possible_hands[-1]

        if action == 2:
            if (hand[0].suit == briscola and hand[1].suit == briscola):
                action = 0

            else:
                possible_hands = []
                for card in hand:
                    if card.suit != briscola:
                        possible_hands.append(card)

                possible_hands.sort(key = lambda x: x.points, reverse = True)
                played_card = possible_hands[0]

        if action == 3:
            if (hand[0].suit == briscola and hand[1].suit == briscola):
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

    else:
        played_card = hand[0]

    return played_card
