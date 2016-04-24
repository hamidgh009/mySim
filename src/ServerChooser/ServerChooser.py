from numpy.core.numeric import inf


class ServerChooser:

    def __init__(self):
        return

    def choose_server(self, vector):
        return vector.index(0)

    def set_decision_pars(self, servers):
        return None


class NthBestServerChooser(ServerChooser):

    n = 2
    servers = None

    def __init__(self, n):
        ServerChooser.__init__(self)
        self.n = n

    def set_decision_pars(self, servers):
        self.servers = servers

    def get_nth_best(self, vector):
        vector_copy = []
        for i in vector:
            vector_copy.append(i)
        temp = []
        while temp.__len__() < self.n:
            index = vector_copy.index(min(vector_copy))
            temp.append(index)
            vector_copy[index] = inf
        return temp

    def get_min_queue(self, indexes):
        mini = inf
        ans = None
        for i in indexes:
            if mini > self.servers[i].get_queue_state():
                mini = self.servers[i].get_queue_state()
                ans = i
        return ans

    def choose_server(self, vector):
        indexes = self.get_nth_best(vector)
        return self.get_min_queue(indexes)
