import math
from operator import indexOf
from tabulate import tabulate

# A1, A2, ...
# COORDINATES = [(x1, y1), (x2, y2), (x3, y3)]
# COORDINATES = [(2,10), (2,5), (8,4), (5,8), (7,5), (6,4), (1,2), (4,9)]
# COORDINATES = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9), (7, 50)]
COORDINATES = [(7.1,5.2), (3.4,4), (9.9,8.7), (1.2,3.4), (5.6,5.9), (8.5,3.4), (2.3,5.2), (1.2,6.7)]

# Length corresponds to K.
INITIAL_CENTROID_INDICES = [0, 1, 2]
# INITIAL_CENTROID_INDICES = [0, 1, 3, 6]

# False for Manhattan Distance
EUCLIDEAN = True


def getHeader():
	head = ["Coordinate"]

	for i in range(len(INITIAL_CENTROID_INDICES)):
		head.append(f"Cluster {i + 1} dist")

	head.append("Cluster")
	return head


def calculate_clustering():
  output = []
  centroids = []
  for i in INITIAL_CENTROID_INDICES:
    centroids.append(COORDINATES[i])

  nbIterations = 0
  stop = False

  while(not stop):
    nbIterations = nbIterations + 1
		
    print(f"Iteration {nbIterations}\n")
    output = []

    clustersInOrder = []
    # Checking in which cluster is each point
    for c in COORDINATES:
      coordinate_output = [c]
      
      distances = []
      for center in centroids:
        if EUCLIDEAN == True:
          distance = math.sqrt((center[0] - c[0])**2 + (center[1] - c[1])**2)
          distances.append(distance)
          coordinate_output.append(distance)
        else:
          distance = abs(center[0] - c[0]) + abs(center[1] - c[1])
          distances.append(distance)
          coordinate_output.append(distance)

      clustersInOrder.append(centroids[indexOf(distances, min(distances))])
      coordinate_output.append(indexOf(centroids, centroids[indexOf(distances, min(distances))]) + 1)
      output.append(coordinate_output)

    print(f"\n Centroids: { centroids } \n")

    # Calculating each cluster position
    newCentroids = []
    for center in centroids:
      indexes = [i for i,x in enumerate(clustersInOrder) if x == center]
      totalx = 0
      totaly = 0
      for i in indexes:
        totalx += COORDINATES[i][0]
        totaly += COORDINATES[i][1]
      newCentroids.append(((totalx/len(indexes)), (totaly/len(indexes))))

    if centroids == newCentroids:
      stop = True
    else:
      centroids = newCentroids

    output = [getHeader(), *output]
    print(tabulate(output, headers='firstrow', tablefmt="grid"))
    print()

  print(f"Used EUCLIDEAN: { EUCLIDEAN }")
  print(f"\nTotal number of iterations: { nbIterations }\n\nFinal centroid coordinates:\n")
  print(f"Centroids: { centroids } \n")


calculate_clustering()