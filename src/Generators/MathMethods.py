import random
import math


class MathMethods:

    def __init__(self):
        return

    @staticmethod
    def find_number_exponential(lambd):
        ans = ((-1)/lambd) * math.log(1-random.random(), 2)
        return ans

    @staticmethod
    def find_number_linear(lambd):
        return 1/lambd
