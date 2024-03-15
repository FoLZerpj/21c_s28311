import abc

class SquareGenerator(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def generate(self, start, end):
        if end < start:
            raise IndexError("End index should be after start index")
        return [x*x for x in range(start, end + 1)]