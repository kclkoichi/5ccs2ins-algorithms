def calculate_regression(cooridinates):
    def calculate_mean_of_x():
        total = 0
        for cooridinate in cooridinates:
            total += cooridinate[0]
        return total/ len(cooridinates)

    def calculate_mean_of_y():
        total = 0
        for cooridinate in cooridinates:
            total += cooridinate[1]
        return total/ len(cooridinates)

    mean_of_x = calculate_mean_of_x()
    mean_of_y = calculate_mean_of_y()

    def calculate_numerator():
        total = 0
        for cooridinate in cooridinates:
            total += (cooridinate[0]-mean_of_x) * (cooridinate[1]-mean_of_y)
        return total

    def calculate_denominator():
        total = 0
        for cooridinate in cooridinates:
            total += (cooridinate[0]-mean_of_x) * (cooridinate[0]-mean_of_x)
        return total

    def calculate_gradient():
        return calculate_numerator() / calculate_denominator()

    gradient = calculate_gradient()

    def calculate_intercept():
        return mean_of_y - gradient * mean_of_x

    intercept = calculate_intercept()

    return (intercept, gradient)

# Change the coordinates and run this file for the out put eg:
# COORDINATES = [(x1, y1), (x2, y2), (x3, y3)]

# COORDINATES = [(35, 78), (42,90), (17, 36)]
COORDINATES = [(2, 2), (4, 3)]

(intercept, gradient) = calculate_regression(COORDINATES)
print(f"Equation: y = {intercept} + {gradient} x")