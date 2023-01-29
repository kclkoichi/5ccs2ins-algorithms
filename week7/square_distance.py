def calculate_distance(coordinates, equation):
    total = 0
    for coordinate in coordinates:
        val = (coordinate[1] - equation(coordinate[0]))**2
        print(f"Coordinate: { coordinate } \n Squared distance: { val }")
        total += val
    return total

# Change the coordinates and run this file for the out put eg:
# COORDINATES = [(x1, y1), (x2, y2), (x3, y3)]

COORDINATES = [(35, 78), (42,90), (17, 36)]

# This is the input linear equation the return value is what y would be eg y = x:
# lambda x : x

equation = lambda x : -0.7575150300601337 + 2.1943887775551105 * x

squared_distance= calculate_distance(COORDINATES, equation)
print(f"Total squared distance: {squared_distance}")