import typing
from typing import Union, Literal
class Card:
    def __init__(self, name: str, types: Literal['Epic', 'Rare', 'Legendary']) -> None:
        self.name = name
        self.types = types

    def intro(self):
        raise NotImplementedError ('your must introduce yourself first')
    