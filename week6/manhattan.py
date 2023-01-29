import math

# COORDINATE = [x, y, z, ...]
# Dimension is implied from it, both should be of same length
COORDINATE1 = [1,3,4,5,2]
COORDINATE2 = [1,4,2,3,2]

def manhattan():
  index = 0
  total = 0
  while(index < len(COORDINATE1)):
    total += abs(COORDINATE1[index] - COORDINATE2[index])
    index = index + 1
  
  return total

print(manhattan())