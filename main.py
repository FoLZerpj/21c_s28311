l = [x*x for x in range(1, 11)]

def e_squares(start, end):
    return [x*x for x in range(start, end + 1)]

class SquareGenerator:
    def generate(self, start, end):
        return [x*x for x in range(start, end + 1)]