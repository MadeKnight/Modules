from random import randint
from pprint import pprint
from chess import *

max_number = 8

def create_random_position():
  return (randint(1,9), randint(1,9))

queens_positions = [create_random_position() for x in range(max_number)]
pprint(queens_positions)
result = is_attacking(queens_positions)
print(result)
