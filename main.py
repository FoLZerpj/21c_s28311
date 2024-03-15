import math

from square_generator.square_generator import SquareGenerator

l = [x*x for x in range(1, 11)]

def e_squares(start, end):
    return [x*x for x in range(start, end + 1)]

generator = SquareGenerator()
lst = generator.generate(1, 10)
sqrt_result_lst = [math.sqrt(x) for x in lst]