from random import randint


class CVGenerator:

    vector_size = 0

    def __init__(self, vector_size):
        self.vector_size = vector_size

    def define_min(self):
        return randint(0, self.vector_size-1)

    def generate_vector(self):
        minim = self.define_min()
        vector = []
        for i in range(0, self.vector_size):
            if i == minim:
                vector.append(0)
            else:
                vector.append(1)
        return vector


class LinearCVGenerator(CVGenerator):

    min_cost = 0
    inc_num = 0

    def __init__(self, vector_size, min_cost, inc_num):
        self.vector_size = vector_size
        self.min_cost = min_cost
        self.inc_num = inc_num

    def generate_vector(self):
        minim = self.define_min()
        vector = []
        for i in range(0, self.vector_size):
            vector.append((abs(i - minim) * self.inc_num) + self.min_cost)
        return vector
