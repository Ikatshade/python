from card_game import Card
from typing import Union, Literal


class Epic(Card):
    def __init__(self, name) -> None:
        super().__init__(name, Epic)