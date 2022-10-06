# Briscola AI

A repo containing AI designed to play Briscola, the classic
Italian card game.

# How to play Briscola

Briscola is played using an Italian card deck, which contains
40 cards instead of the 52 card deck that's normally used in
North America. The value of the cards and the face value are
different from each other:

|face value  | point value |
| ---------- | ----------- |
|A           |    11       |
|2           |    0        |
|3           |    10       |
|4           |    0        |
|5           |    0        |
|6           |    0        |
|7           |    0        |
|J           |    2        |
|Q           |    3        |
|K           |    4        |

which comes to a total of 120 points in a deck. When you place
a card, the opponent can capture it in 2 ways:

- place down a higher value card from the same suit
- place down a card from the Briscola suit

If the opponent doesn't capture your card, then you take both of
them. Whoever gets the cards gets to draw first and plays first next.
The suit that becomes the Briscola is decided at the start of every
game.

# What's in the Repo

This project is still a work in progress, so bugs are expected.
Right now, the repo contains a working set of functions that train
a player class to play Briscola with Markov decision processes.

# TODO

- Add interface to play against the AI
- Add neural network

#License

This repo is licensed under the GPL 3.
