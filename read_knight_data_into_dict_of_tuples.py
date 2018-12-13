#!/usr/bin/env python
"""
Splendid demo for KAPL class on proper file layout.

"""
from pprint import pprint

def main():
    """
    Program entry point.

    :return: None
    """
    d = read_data()
    pretty_print_data(d)
    print()
    print_data_for_knight("Lancelot", d)
    print()
    print_titles_and_names(d)

def read_data():
    """
    Read knight data from flat colon-delimited file.
    Returns dictionary in format KNIGHT_NAME:INFO_TUPLE

    :return: Dictionary of knight data
    """
    knight_data = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print_data(data):
    """
    Dump knight data to screen

    :param data: dict of data
    :return: None
    """

    pprint(data)

def print_data_for_knight(knight, data):
    """
    Display details for one knight

    :param knight: Name of knight
    :param data: Dict of knight data
    :return: None
    """
    print(data[knight])

def print_titles_and_names(data):
    """
    Output all knights with their titles and quests.

    :param data: Dict of data
    :return: None
    """
    #    key  value (which is tuple of things)
    for name, info in data.items():
        print(f"{info[0]} {name} seeks ... {info[2]}")

if __name__ == '__main__':
    main()










