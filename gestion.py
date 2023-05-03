from pathlib import Path
import re
import string
from tinydb import TinyDB, where

class User:

    db = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str ,last_name: str, number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address

    def __str__(self) -> str:
        return f'{self.full_name}\n{self.number}\n{self.address}\n'
    
    def __repr__(self) -> str:
        return f"User{self.first_name}, {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self):
        return User.db.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))
    

    def _check(self):
        self._check_phone_number()
        self._check_names()

    def _check_phone_number(self):
        digits = re.sub(r"[+()\s]*", "", self.number)
        if len(digits) < 10 or not digits.isdigit():
            raise ValueError(f'Number {self.number} not valid')
        
    def _check_names(self):
        if not(self.first_name and self.last_name):
            raise ValueError("First name and last name can not be empty.")
        special_characters = string.punctuation + string.digits
        for i in self.first_name + self.last_name:
            if i in special_characters:
                raise ValueError(f"Name invalid {self.full_name}.")

    def exist(self):
        return bool(self.db_instance)
    

    def delete(self) -> list[int]:
        if self.exist():
            return User.db.remove(doc_ids = [self.db_instance.doc_id])
        return []


    def save(self, validate_data = False):
        if validate_data:
            self._check()
        
        if self.exist():
            return -1
        else:
            return User.db.insert(self.__dict__)


def get_all_users():
    return [User(**user) for user in User.db.all()]
        

if __name__ == "__main__":
    m = User("Rosie", "Clarke")
    print(m.delete())
    # from faker import Faker
    # fake = Faker(locale="en_UK")
    # for i in range (10):
    #     user = User(first_name = fake.first_name(),
    #                 last_name = fake.last_name(),
    #                 number = fake.phone_number(),
    #                 address = fake.address())
    #     print(user.save())
    #     print("-" * 10)

