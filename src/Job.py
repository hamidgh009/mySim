class Job:
    enter_time = 0
    limit_time = 0
    process_time = 0
    forward_cost = 0

    def __init__(self, enter_time, limit_time, process_time, forward_cost):
        self.enter_time = enter_time
        self.limit_time = limit_time
        self.process_time = process_time
        self.forward_cost = forward_cost

    def get_finish_time(self, now):
        return now + self.process_time

    def get_leave_time(self):
        return self.enter_time + self.limit_time