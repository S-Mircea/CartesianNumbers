#import the math library to get access to square roots
import math

#list of points on the cartesian plane
points = [(0,0),(2,3),(4,1),(1,2),(5,5),(7,2),(9,6)]

#initialize the closest_distance and closest_points variables
closest_distance = float("inf")
closest_points = ()

#iterate through the list of points
for (x1,y1) in points:
  for (x2,y2) in points:
    #only calculate the distance between two points if they are different
    if (x1,y1) != (x2,y2):
      #calculate the distance between two points using the distance formula
      distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
      #if the newly calculated distance is smaller than the current closest_distance
      if distance < closest_distance:
        #update the closest_distance and closest_points variables
        closest_distance = distance
closest_points = ((x1,y1),(x2,y2))

#print the closest points
print("The closest points are:", closest_points)