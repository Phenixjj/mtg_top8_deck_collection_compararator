import argparse

import csv
from tkinter.ttk import Separator


def deck_comparator(mtgDeck, collection):
    # print(mtgDeck, collection)
    # print('coucou')
    full_cards_collection = open(collection, 'r')
    cards_name_collection = []
    cards_name_top8 = []
    personal_card = []
    missed_cards = []
    file = csv.DictReader(full_cards_collection, delimiter=';')
    for col in file:
        cards_name_collection.append(col['Name'])
    # print("========== CARDS NAME COLLECTION ============\n", cards_name_collection)
    deck_top8 = open(deckTop8, 'r')
    lines = deck_top8.readlines()
    for line in lines:
        cards_name_top8.append(line.strip('\n'))
    # print("========== CARDS NAME DECK TOP 8 ============\n", cards_name_top8)
    for card in cards_name_top8:
        if card in cards_name_collection:
            personal_card.append(card)
        elif card not in cards_name_collection:
            missed_cards.append(card)
    
    print("*** YOU HAVE " + str(len(personal_card)) + " % OF " + str((mtgDeck).split('.')[0]).upper() + " DECK ***\n")
    print('================================================================================================')
    print("CARDS IN YOUR POSSESSION : \n")
    print(personal_card)
    print('================================================================================================')
    print("MISSED CARDS : \n")
    print(missed_cards)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--top8', default="")
    parser.add_argument('--collection', default="collection.csv")
    args = parser.parse_args()
    deckTop8 = args.top8
    collection = args.collection
    deck_comparator(deckTop8, collection)