import scrython
import time

class Card():
    def __init__(self, name):
        self.name = name
    
    def get_img(name):
        time.sleep(0.1)
        card = scrython.cards.Named(fuzzy=name)
        card_image = card.image_uris()
        card_image_large = card_image['large']
        return card_image_large