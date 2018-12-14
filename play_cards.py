#!/usr/bin/env python
from carddeck import CardDeck, JokerDeck

d1 = CardDeck("Anne")
print(d1)
print(type(d1), '\n')
d2 = CardDeck("Will")

print(d1.get_dealer())

d1.set_dealer("Fred")
print(d1.get_dealer())

print(d1.dealer)

d1.dealer = 'Abe'

print(d1.dealer)

try:
    d1.dealer = 123
except TypeError as err:
    print(err)

d1.shuffle()

print(d1.cards)

print()
for i in range(5):
    print(d1.draw())
print('\n')

j1 = JokerDeck('Fiona')
j1.shuffle()
print(j1.draw())
print()
print(j1.cards)

print(len(d1))
print(len(j1))

print(d1)
print(j1)
print(JokerDeck.mro())
