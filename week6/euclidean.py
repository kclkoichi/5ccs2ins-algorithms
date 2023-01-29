import math

# COORDINATE = [x, y, z, ...]
# Dimension is implied from it, both should be of same length
COORDINATE1 = [0,2,4,4,5,8]
COORDINATE2 = [4,2,1,1,7,1]

def euclidean():
  index = 0
  total = 0
  while(index < len(COORDINATE1)):
    total += (COORDINATE1[index] - COORDINATE2[index])**2
    index = index + 1
  
  return math.sqrt(total)

print(euclidean())