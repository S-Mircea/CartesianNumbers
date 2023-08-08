#import matplotlib.pyplot as plt
from random import randint
from heapq import heappush, heappop, heapify
from math import sqrt

def distance(pointA, pointB):
    return sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)

def closest(points, k, origin):
    heap = []
    for point in points[:k]:
        heappush(heap, point)

    for point in points[k:]:
        if distance(point, origin) < distance(heap[0], origin):
            heappop(heap)
            heappush(heap, point)
    return heap

def naive(points, k, origin):
    sortedPoints = sorted(points, key=lambda p: distance(p, origin))
    return sortedPoints[:k]

points = [(randint(0, 100), randint(0, 100)) for i in range(100)]
k = 4
resA = closest(points, k, (0, 0))
resB = naive(points, k, (0, 0))
#plt.scatter(*zip(*points))
#plt.scatter(*zip(*resA))
#plt.scatter(*zip(*resB))
#plt.show()