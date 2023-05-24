'''
This exercise is to locate things in a random map
a random map will be generated, its dimensions left to right (x) will be the same as the dimensions top to bottom (y)
the coordinates will start at the top left of the map and will start at 0 for both x, and y
The map contains two objects
a player 'p' and a target 't'
your task is to write some code to find the coordinates of both and print them to the screen.

map is a random map containing the two objects, it changes each time this is run
'''

# the following code sets the start, do not modify it
from random import randint

import RandomMapGen

map = RandomMapGen.get_random_map(randint(5, 20))

######## Your code below :


