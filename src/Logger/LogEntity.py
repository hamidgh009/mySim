class LogEntity:

    cost = 0
    enter_time = 0
    end_time = 0
    status = ""

    def __init__(self, cost, enter_time, end_time, status):
        self.cost = cost
        self.end_time = end_time
        self.enter_time = enter_time
        self.status = status
