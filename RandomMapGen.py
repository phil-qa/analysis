import random

def get_random_map(size):
    # initialise empty
    map = []
    for y in range(size):
        map_x = []
        for x in range(size):
            map_x.append(0)
        map.append(map_x)

    player = [random.randint(0,size - 1), random.randint(0, size -1)]
    target = [random.randint(0,size - 1), random.randint(0, size -1)]
    while target == player:
        target = [random.randint(0,size - 1), random.randint(0, size -1)]

    map[player[0]] [player[1]] = 'p'
    map[target[0]] [target[1]] = 't'

    return map

