"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""
class player():
    def _init_(self):
        self.points = 0
        self.wins = 0
        self.hand = []
        self.state_array = []
        #If they have the better hand
        self.best = False
        #Maps state_array and action to Q value
        self.Q_values = {}
        self.gamma = 0
        self.learning_rate = 0

    def get_best_action(self, key):
        best_action = -1
        best_Q = -1000

        for i in range(0, 4):
            try:
                candidate = key.copy()
                candidate.append(i)
                Q = self.Q_values[tuple(candidate)]
                if Q > best_Q:
                    best_Q = Q
                    best_action = i

            except KeyError:
                pass

        return best_action

    def learn(self, reward, new_state, current_action):
        key = self.state_array.copy()
        key.append(current_action)

        if len(self.state_array) < 5:
            new_state_array = self.state_array.copy()

        else:
            new_state_array = self.state_array[1:]

        new_state_array.append(new_state)

        if tuple(key) not in self.Q_values:
            self.Q_values[tuple(key)] = 1000

        best_action = self.get_best_action(new_state_array)

        if best_action == -1:
            new_key = new_state_array + [0]
            self.Q_values[tuple(new_key)] = 1000

        else:
            new_key = new_state_array + list(best_action)

        next_Q = self.Q_values[tuple(new_key)]
        current_Q = self.Q_values[tuple(key)]
        self.Q_values[tuple(key)] = current_Q + self.learning_rate * (reward + self.gamma * next_Q - current_Q)

        self.state = new_state_array

    def play_card(self, opponent, briscola):
        action = max(0, self.get_best_action(self.state_array))
        played_card = None

        if action == 0:
            possible_hands = []
            for card in self.hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            if len(possible_hands) == 0:
                action = 2

            else:
                possible_hands.sort(key = lambda x: x.points, reverse = True)
                played_card = possible_hands[0]

        elif action == 1:
            possible_hands = []
            for card in self.hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            possible_hands[-1]

        elif action == 2:
            possible_hands = []
            for card in self.hand:
                if card.suit != briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[0]

        else:
            possible_hands = []
            for card in self.hand:
                if card.suit != briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)

            if len(possible_hands) == 0:
                action = 0

            else:
                played_card = possible_hands[-1]

        if action == 0:
            possible_hands = []
            for card in self.hand:
                if card.suit == briscola:
                    possible_hands.append(card)

            possible_hands.sort(key = lambda x: x.points, reverse = True)
            played_card = possible_hands[0]

        return played_card
