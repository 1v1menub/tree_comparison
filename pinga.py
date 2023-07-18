from ss_tree import SSTree  
import numpy as np
import random

sstree = SSTree(M=4, m=2)

def get_elements(num_dimensions, num_elements):
    points = []
    for _ in range(num_elements):
        coordinates = [random.randint(-1000, 1001) for _ in range(num_dimensions)]
        points.append(coordinates)
    return points

elements = get_elements(2, 50)
for e in elements:
    sstree.insert(np.array(e))

#GAAAAA

sstree.print()