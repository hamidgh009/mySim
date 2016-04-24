import matplotlib.pyplot as plt
from LogEntity import LogEntity


class BaseLogger:

    servedNumber = 0
    blockedNumber = 0
    leavedNumber = 0
    ehtemalServe = {0: 0}
    ehtemalBlock = {0: 0}
    ehtemalLeave = {0: 0}
    blocked_list = []
    served_list = []
    leaved_list = []
    n_cost = {0: 0}
    n_waitingTime = {0: 0}

    def __init__(self):
        self.servedNumber = 0
        self.blockedNumber = 0
        self.leavedNumber = 0
        self.ehtemalServe = {0: 0}
        self.ehtemalBlock = {0: 0}
        self.ehtemalLeave = {0: 0}
        self.n_cost = {0: 0}
        self.n_waitingTime = {0: 0}
        self.blocked_list = []
        self.served_list = []
        self.leaved_list = []

        return

    def add_log(self, cost, enter_time, end_time, final_status):
        if final_status == 'blocked':
            self.blockedNumber += 1
            self.blocked_list.append(LogEntity(cost, enter_time, end_time, final_status))
            # print('blocked')
        elif final_status == 'served':
            self.servedNumber += 1
            self.served_list.append(LogEntity(cost, enter_time, end_time, final_status))
            # print('served')
        else:
            self.leavedNumber += 1
            self.leaved_list.append(LogEntity(cost, enter_time, end_time, final_status))
            # print('leaved')

    def calculate_ehtemalat(self, indicator, all_process):
        self.ehtemalBlock[indicator] = self.blockedNumber/float(all_process)
        self.ehtemalLeave[indicator] = self.leavedNumber/float(all_process)
        self.ehtemalServe[indicator] = self.servedNumber/float(all_process)

    def calculate_cost_waiting(self, n):
        temp_cost = 0
        temp_waiting = 0
        full_num = self.served_list.__len__()
        for i in self.served_list:
            temp_cost += i.cost
            temp_waiting += (i.end_time - i.enter_time)
        self.n_cost[n] = float(temp_cost)/float(full_num)
        self.n_waitingTime[n] = float(temp_waiting)/float(full_num)

    def reset(self):
        self.servedNumber = 0
        self.blockedNumber = 0
        self.leavedNumber = 0
        self.blocked_list = []
        self.served_list = []
        self.leaved_list = []

    def draw_served_probability(self):
        key_parameter = []
        value_parameter = []

        for key, value in self.ehtemalServe.iteritems():
            key_parameter.append(key)

        key_parameter.sort()
        key_parameter.remove(0)
        for key in key_parameter:
            value_parameter.append(self.ehtemalServe[key])

        plt.plot(key_parameter, value_parameter, linewidth=1)
        plt.ylim(0, 1.1)
        plt.ylabel('Serve Probability')
        plt.grid(True)
        plt.legend()
        plt.show()

    def draw_blocked_probability(self):
        key_parameter = []
        value_parameter = []

        for key, value in self.ehtemalBlock.iteritems():
            key_parameter.append(key)

        key_parameter.sort()
        key_parameter.remove(0)
        for key in key_parameter:
            value_parameter.append(self.ehtemalBlock[key])

        plt.plot(key_parameter, value_parameter, linewidth=1)
        plt.ylim(0, 1.1)
        plt.ylabel('Block Probability')
        plt.grid(True)
        plt.legend()
        plt.show()

    def draw_leaved_probability(self):
        key_parameter = []
        value_parameter = []

        for key, value in self.ehtemalLeave.iteritems():
            key_parameter.append(key)

        key_parameter.sort()
        key_parameter.remove(0)
        for key in key_parameter:
            value_parameter.append(self.ehtemalLeave[key])

        plt.plot(key_parameter, value_parameter, linewidth=1)
        plt.ylim(0, 1.1)
        plt.ylabel('Leave Probability')
        plt.grid(True)
        plt.legend()
        plt.show()

    def draw_cost_waiting_time(self):
        key_parameter = []
        costs =[]
        waiting_times = []

        for key, value in self.n_cost.iteritems():
            key_parameter.append(key)
        key_parameter.sort()
        key_parameter.remove(0)

        for key in key_parameter:
            print key
            costs.append(self.n_cost[key])
            waiting_times.append(self.n_waitingTime[key])
            plt.plot(self.n_cost[key], self.n_waitingTime[key], 'ro')
            plt.annotate(str(key), xy=(self.n_cost[key], self.n_waitingTime[key]))
        plt.ylabel('waiting_times')
        plt.xlabel('costs')
        plt.show()
