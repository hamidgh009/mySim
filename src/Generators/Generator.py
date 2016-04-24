import math
from random import random
import numpy as np

class Generator:

    landa = 0
    time_unit = 0

    def __init__(self, landa, time_unit):
        self.landa = landa
        self.time_unit = time_unit

    def generate(self):
        return 0


class ConstantGenerator(Generator):

    def generate(self):
        return self.landa


class FixedGenerator(Generator):

    def generate(self):
        return int((1.0/float(self.landa))*self.time_unit)


class ExponentialGenerator(Generator):

    total = 0
    avg = 0

    def generate(self):
        self.total+=1
        ans = (-math.log(1.0 - random()) / self.landa)*self.time_unit
        self.avg = (((self.total-1) * self.avg) + ans) / float(self.total)

        return ans
