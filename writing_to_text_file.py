#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in fruits:
        fruitdata_out.write(fruit + '\n')


with open('DATA/words.txt') as words_in:
    with open('upperwords.txt', 'w') as words_out:
        for line in words_in:
            words_out.write(line.upper())
