def closest_distances(points, K):
    distance_list = []
    for (x, y) in points:
        distance = (x**2 + y**2)**0.5
        distance_list.append(distance)
        sorted_distances = sorted(distance_list)
    closest = sorted_distances[0:K]
    return closest


