#!/usr/bin/python

from card import *
import csv

def deck(briscola):
    new_deck = []
    with open("every_card.csv", mode ='r') as file:
        csv_file = csv.reader(file)

        for lines in csv_file:
            new_card = card()
            new_card.suit = lines[0]
            new_card.value = lines[1]
            new_card.points = int(lines[2])
            new_card.index = int(lines[3])
            new_card.set_briscola(briscola)

            new_deck.append(new_card)

    return new_deck

