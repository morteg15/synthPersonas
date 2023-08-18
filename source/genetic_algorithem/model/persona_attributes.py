import random

NAMES = ["Alice", "Bob", "Charlie", "Dave"]
AGES = [25, 30, 35, 40]
LOCATIONS = ["Oslo", "Bergen", "Stavanger", "Trondheim"]
INTERESTS = ["Birds", "Mammals", "Reptiles", "Fish"]
ATTRIBUTES = [NAMES, AGES, LOCATIONS, INTERESTS]

def random_persona():
    return [random.choice(NAMES), random.choice(AGES), random.choice(LOCATIONS), random.choice(INTERESTS)]
