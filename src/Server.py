
class Server:
    buffer_size = 0
    jobs = []
    last_process_event = 0

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.last_process_event = 0
        self.jobs = []

    def add_new_job(self, job):
        if self.jobs.__len__() >= self.buffer_size:
            return False
        self.jobs.append(job)
        return True

    def get_next_leave(self):
        if self.jobs.__len__() == 0:
            return None
        min_leave_job = self.jobs[0]
        for i in self.jobs:
            if min_leave_job.get_leave_time() > i.get_leave_time():
                min_leave_job = i
        return min_leave_job

    def get_min_finish(self, now):
        if self.jobs.__len__() == 0:
            return None
        min_finish_job = self.jobs[0]
        for i in self.jobs:
            if min_finish_job.get_finish_time(now) > i.get_finish_time(now):
                min_finish_job = i
        return min_finish_job

    def get_next_finish(self, now):
        if self.jobs.__len__() == 0:
            return None
        return self.jobs[0].get_finish_time(now)

    def get_queue_state(self):
        return self.jobs.__len__()

    def get_next_job(self):
        if self.jobs.__len__() == 0:
            return None
        return self.jobs[0]

    def remove_job_from_queue(self, job):
        self.jobs.remove(job)

    def get_num_of_jobs(self):
        return self.jobs.__len__()

    # yani akhare anjaame process badi
    def get_next_process_event(self, now):
        if self.jobs.__len__() == 0:
            return float('inf')
        elif now < self.last_process_event:
            return self.last_process_event
        else:
            temp_job = self.get_next_job()
            self.last_process_event = temp_job.get_finish_time(now)
        return self.last_process_event
