import math
from cubic_generator import CubicGenerator
from square_generator import SquareGenerator

l = [x*x for x in range(1, 11)]
print("List of squares:", l)

def e_squares(start, end):
    return [x*x for x in range(start, end + 1)]

generator = SquareGenerator()
lst = generator.generate(1, 10)
sqrt_result_lst = [math.sqrt(x) for x in lst]
print("Resulting list of square roots:", sqrt_result_lst)

generator = CubicGenerator()
lst = generator.generate(1, 10)
print("List received from CubicGenerator:", lst)