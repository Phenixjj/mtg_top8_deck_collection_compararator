import scrython
import time

def get_card(card):
    time.sleep(0.1)
    card = scrython.cards.Named(fuzzy=card)
    card_image = card.image_uris()
    card_image_large = card_image['large']
    return card_image_large

if __name__ == "__main__":
    card_name = str(input("Enter the name of mtg card : "))
    print("*** CARD NAME \n", card_name)
    card = get_card(card_name)
    print(card)
    import pdb
    pdb.set_trace()