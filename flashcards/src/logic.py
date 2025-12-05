from .data_handler import load_data
import random


class FlashManager:
    def __init__(self, cards, shuffle = False):
        self.cards = cards.copy()
        if shuffle:
            random.shuffle(self.cards)

        self.current_index = 0
        self.showing_back = False