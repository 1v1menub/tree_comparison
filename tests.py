from mtree import MTree
from ss_tree import SSTree
import numpy as np
import random
import math
import time


def d_int(point1, point2): 
    squared_distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

mtree = MTree(d_int, max_node_size=50)
sstree = SSTree(M=50, m=25)

def get_elements(num_dimensions, num_elements):
    points = []
    for _ in range(num_elements):
        coordinates = [random.randint(-1000, 1001) for _ in range(num_dimensions)]
        points.append(coordinates)
    return points

elements = get_elements(20, 1000)

startime1 = time.time()
mtree.add_all(elements)

for i in elements:
    sstree.insert(i)

endtime1 = time.time()
print(f"Tiempo en insertar: {(endtime1 - startime1):.5f} segundos")

print("------------------------------------------------")

query = []
for i in range(20):
    query.append(0)

startime2 = time.time()
result = mtree.search(query, 5)
endtime2 = time.time()
""" print(list(result)) """
print(f"Tiempo en buscar k = 5: {(endtime2 - startime2):.5f} segundos")

