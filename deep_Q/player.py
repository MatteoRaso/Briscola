"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""
import numpy as np
from tensorflow.keras.layers import Conv1D, Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.models import Sequential
from tensorflow.keras import Input

class player():
    def __init__(self):
        self.points = 0
        self.wins = 0
        self.hand = []
        self.state_array = []
        self.memory = []
        self.memory_size = 10000
        self.batch_size = 32
        self.rng = np.random.default_rng()
        self.Q = Sequential()
        self.gamma = 0.15
        self.exploration = 0.3

    def _init_model(self):
        self.Q.add(Input(shape=(5, 41)))
        self.Q.add(Conv1D(16, 8, strides=4, activation='relu', padding='same'))
        self.Q.add(Conv1D(32, 4, strides=2, activation='relu', padding='same'))
        self.Q.add(Dense(256, activation='relu'))
        self.Q.add(Dense(40))
        self.Q.compile(loss="MeanSquaredError", metrics=['accuracy'])
        self.Q.build()

    def _process_state(self, state):
        # Feature 0: Cards won by the AI
        # Feature 1: Cards won by opponent
        # Feature 2: Cards in hand
        # Feature 3: Face card
        # Feature 4: Score
        F_0 = np.zeros(41)
        F_0[np.where(state == 1)] = 1

        F_1 = np.zeros(41)
        F_1[np.where(state == -1)] = 1

        F_2 = np.zeros(41)
        F_2[np.where(state == 2)] = 1

        F_3 = np.zeros(41)
        F_3[np.where(state == 3)] = 1

        F_4 = np.zeros(41)
        F_4[-1] = 1

        processed_state = np.array([])
        processed_state = np.vstack((processed_state, F_0))
        processed_state = np.vstack((processed_state, F_1))
        processed_state = np.vstack((processed_state, F_2))
        processed_state = np.vstack((processed_state, F_3))
        processed_state = np.vstack((processed_state, F_4))

        return processed_state

    def _get_action(self, explore=True):
        if explore and (self.exploration > self.rng.uniform()):
                action = self.hand[self.rng.integers(0, 3)].index

        else:
                action_array = self.Q.output(self.state_array)
                mask = np.zeros(41)
                for card in self.hand:
                    mask[card.index] = 1

                action_array = np.ma.masked_array(action_array, mask=mask)
                action = np.where(action_array == np.max(action_array))

        return action

    def add_memory(self, state_0, action, reward, state_1):
        state_0 = self._process_state(state_0)
        state_1 = self._process_state(state_1)
        new_memory = (state_0, action, reward, state_1)
        self.memory.append(new_memory)

    def train_model(self):
        if len(self.memory) > self.memory_size:
            diff = len(self.memory) - self.memory_size
            self.memory = self.memory[diff:]

        if len(self.memory) == self.memory_size:
            batch = self.rng.choice(self.memory, replace=False)
            x = np.array([])
            y = np.array([])
            for element in batch:
                x_Q_output = self.Q.output(element[0])
                x_quality = x_Q_output[element[1]]
                x = np.append(x, x_quality)

                if 0 not in element[3]:
                    y = np.append(y, element[2])

                else:
                    Q_output = self.Q.output(element[3])
                    mask = np.zeros(41)
                    for card in self.hand:
                        mask[card.index] = 1

                    Q_output = np.ma.masked_array(Q_output, mask=mask)
                    quality = element[2] + self.gamma * np.max(Q_output)
                    y = np.append(y, quality)

            self.Q.train_on_batch(x, y)

    def play_card(self, opponent, briscola, explore=True):
        if len(self.hand) == 0:
            pass

        else:
            action = self._get_action(explore)
            for card in self.hand:
                if card.index == action:
                    played_card = card
                    break

        return played_card

