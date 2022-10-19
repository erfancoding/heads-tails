# Head and Tails Game
import random

Heads = 0
Tails = 1
random_choice = random.randint(Heads, Tails)

if random_choice == Heads:
    print("Heads")
else:
    print("Tails")
