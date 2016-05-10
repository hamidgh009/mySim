
import matplotlib.pyplot as plt
from BaseLogger import *
import math


class GraphLogger(BaseLogger):

    si1Samples = {0: 0}   # tedade node haa ba vazne > i
    xiSamples = {0: 0}    # tedaade node haa ba vazne i
    siSamples = {0: 0}   # tedade node haa ba vazne >= i
    e1iSamples = {0: 0}   # tedaade edge haa k har 2 ras dar xi bashad
    e2iSamples = {0: 0}   # tedaade edge haa k 1 ras dar xi va 1 ras dar si1 baashad
    sampleNum = 0
    i =0
    graph = None
    logRate = 1
    lognum = 0

    def __init__(self, graph, logRate, i):
        super(GraphLogger, self).__init__()
        self.si1Samples = {0: 0}
        self.siSamples = {0: 0}
        self.xiSamples = {0: 0}
        self.e1iSamples = {0: 0}
        self.e2iSamples = {0: 0}
        self.sampleNum = 0
        self.i = i
        self.graph = graph
        self.logRate=logRate
        self.lognum = 0
        return

    def add_sample(self, servers):

        if self.lognum < (1/self.logRate):
            self.lognum += 1
            return

        self.lognum -= (1/self.logRate)
        self.sampleNum += 1
        si1nodes = []
        xinodes = []
        sinodes = []
        for s in servers:
            if s.get_queue_state() == self.i:
                xinodes.append(servers.index(s))
                sinodes.append(servers.index(s))
            elif s.get_queue_state() > self.i:
                si1nodes.append(servers.index(s))
                sinodes.append(servers.index(s))
        self.si1Samples[self.sampleNum] = si1nodes.__len__()
        self.siSamples[self.sampleNum] = sinodes.__len__()
        self.xiSamples[self.sampleNum] = xinodes.__len__()
        self.e1iSamples[self.sampleNum] = self.graph.get_edges_num(xinodes)

        temp =0
        for j in xinodes:
            for k in si1nodes:
                if self.graph.has_edge(j, k):
                    temp += 1
        self.e2iSamples[self.sampleNum] = temp

        print self.sampleNum

    def draw_samples_graph1(self, p):
        # Ei and Xi^2*p/2
        key_parameter = []
        value_parameter = []
        for key, value in self.xiSamples.iteritems():
            key_parameter.append(key)
        key_parameter.sort()
        for key in key_parameter:
        plt.plot(key_parameter, value_parameter, 'ro', markersize=4, color='b')

        key_parameter = []
        value_parameter = []
        for key, value in self.e1iSamples.iteritems():
            key_parameter.append(key)
        plt.plot(key_parameter, value_parameter, 'ro', markersize=4, color='r')

        plt.ylabel('Ei and Xi^2*p/2')
        plt.grid(True)
        plt.legend()
        plt.show()

    def draw_samples_graph2(self, p):
        key_parameter = []
        value_parameter = []
        for key, value in self.xiSamples.iteritems():
            key_parameter.append(key)
        key_parameter.sort()
        for key in key_parameter:
        plt.plot(key_parameter, value_parameter, 'ro', markersize=4, color='b')

        key_parameter = []
        value_parameter = []
        for key, value in self.e2iSamples.iteritems():
            key_parameter.append(key)
        plt.plot(key_parameter, value_parameter, 'ro', markersize=4, color='r')

        plt.grid(True)
        plt.legend()
        plt.show()

