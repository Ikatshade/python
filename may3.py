import random

class Man:

    def __init__(self, first_name: str ,last_name: str, meal: str, step_number: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.meal = meal
        self.step_number = step_number

    def intro(self):
        return f'My name is {self.first_name} {self.last_name}'
    
    # @property
    # def fullname(self):
    #     return f'{self.first_name} {self.last_name}'
    
    def walk(self):
        return f'I made {self.step_number} steps'
    
    def eat(self):
        return f'I am eating {self.meal}'

# fréjus = Man('KOFFI', 'Koffi Fréjus', 'garba')
# print(fréjus.eat())




class Character:

    def __init__(self, points: int = 0) :
        self.points = points

    def roll_dice(self):
        roll = random.randint(1, 7)
        self.points += roll
        return self.points
    
    def get_result(self):
        return f'with {self.points}'
    

p = Character()
m = Character()

for i in range(3):
    p.roll_dice()
    m.roll_dice()

result_p = p.get_result()
result_m = m.get_result()

print('M won ' + result_m if result_m > result_p else 'P won ' + result_p)
