import scrython
import time
# import asyncio

def get_img(name):
        time.sleep(0.1)
        print("===== IN GET IMG ======")
        print("===== NAME => ", name)
        card = scrython.cards.Named(fuzzy=name)
        print("===== CARD ======\n", card)
        card_image = card.image_uris()
        card_image_large = card_image['large']
        return card_image_large

class Card():
    def __init__(self, name):
        self.name = name
        self.image = get_img(name=name)
    
    # async def get_img(name):
    #     time.sleep(0.1)
    #     print("===== IN GET IMG ======")
    #     print("===== NAME => ", name)
    #     card = await scrython.cards.Named(fuzzy=name)
    #     print("===== CARD ======\n", card)
    #     card_image = card.image_uris()
    #     card_image_large = card_image['large']
    #     return card_image_large