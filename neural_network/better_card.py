"""
This file is part of Briscola.

Briscola is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Briscola is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Briscola. If not, see <https://www.gnu.org/licenses/>.
"""
def better_card(card_1, card_2, briscola):

    total_points = card_1.points + card_2.points

    if card_1.suit == card_2.suit:
        if card_1.points >= card_2.points:
            return total_points

        else:
            #Negative output will mean that the
            #second player takes the points.
            return -total_points

    elif card_2.suit == briscola:
        return -total_points

    return total_points
