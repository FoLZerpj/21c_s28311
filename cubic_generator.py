
from square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate(self, start, end):
        if end < start:
            raise IndexError("End index should be after start index")
        return [x*x*x for x in range(start, end + 1)]