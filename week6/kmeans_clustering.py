import math
from operator import indexOf

# A1, A2, ...
# COORDINATES = [(x1, y1), (x2, y2), (x3, y3)]
COORDINATES = [(2,10), (2,5), (8,4), (5,8), (7,5), (6,4), (1,2), (4,9)]

# Length corresponds to K.
INITIAL_CENTROID_INDICES = [0, 3, 6]

# False for Manhattan Distance
EUCLIDEAN = False

def calculate_clustering():
  centroids = []
  for i in INITIAL_CENTROID_INDICES:
    centroids.append(COORDINATES[i])

  nbIterations = 0
  stop = False

  while(not stop):
    nbIterations = nbIterations + 1

    clustersInOrder = []
    # Checking in which cluster is each point
    for c in COORDINATES:
      distances = []
      for center in centroids:
        if EUCLIDEAN == True:
          distances.append(math.sqrt((center[0] - c[0])**2 + (center[1] - c[1])**2))
        else:
          distances.append(abs(center[0] - c[0]) + abs(center[1] - c[1]))

      clustersInOrder.append(centroids[indexOf(distances, min(distances))])

    # Printing info of which coordinate is in which cluster
    print(COORDINATES)
    for c in clustersInOrder:
      print(indexOf(centroids, c), end=' ')
    print(f"\nActual centroids: { centroids } \n")

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

  print(f"Used EUCLIDEAN: { EUCLIDEAN }")
  print(f"Total number of iterations: { nbIterations }\nFinal centroid coordinates:")
  for c in centroids:
    print(f"{ c }")

calculate_clustering()