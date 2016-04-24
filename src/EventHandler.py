import Main
import Server
import Job


class EventHandler:

    logger = None
    servers = []

    next_enter_event = 0
    last_enter_event = 0

    server_of_next_process = None

    generated_jobs = 0

    cv_generator = None
    entrance_generator = None
    limit_time_generator = None
    process_time_generator = None
    server_chooser = None

    def __init__(self, logger, entrance_gen, limit_time_gen, process_time_gen, cv_gen, server_chooser):
        self.servers = []
        for i in range(0, Main.number_of_servers):
            self.servers.append(Server.Server(Main.server_buffer_size))
        self.generated_jobs = 0
        self.next_enter_event = -1
        self.last_enter_event = 0
        self.next_process_event = -1
        self.logger = logger
        self.entrance_generator = entrance_gen
        self.limit_time_generator = limit_time_gen
        self.process_time_generator = process_time_gen
        self.server_chooser = server_chooser
        self.server_of_next_process = None
        self.cv_generator = cv_gen

    def get_next_enter_event(self, lastee):
        if self.next_enter_event == -1:
            self.next_enter_event = lastee + self.entrance_generator.generate()
        self.last_enter_event = self.next_enter_event
        return self.next_enter_event

    def get_next_process_event(self, now):

        temp_time = float('inf')
        temp_server = None
        for i in self.servers:
            if i.get_next_process_event(now) < temp_time:
                temp_time = i.get_next_process_event(now)
                temp_server = i
        self.server_of_next_process = temp_server

        return temp_time

    def get_next_leave_event(self):
        temp = float('inf')
        for i in self.servers:
            if i.get_next_leave() is None:
                continue
            if i.get_next_leave().get_leave_time() < temp:
                temp = i.get_next_leave().get_leave_time()
        return temp

    def add_new_process(self, now):
        temp_cv = self.cv_generator.generate_vector()
        self.server_chooser.set_decision_pars(self.servers)
        server_number = self.server_chooser.choose_server(temp_cv)
        temp_job = Job.Job(now, self.limit_time_generator.generate(),
                           self.process_time_generator.generate(), temp_cv[server_number])
        added = self.servers[server_number].add_new_job(temp_job)
        if not added:
            self.logger.add_log(temp_job.forward_cost, temp_job.enter_time, temp_job.enter_time, 'blocked')
        return

    def remove_leave_event_job(self):
        temp_server = self.servers[0]
        temp_job = self.servers[0].get_next_leave()
        for i in self.servers:
            if temp_job is None or (i.get_next_leave() is not None and i.get_next_leave().get_leave_time() < temp_job.get_leave_time()):
                temp_job = i.get_next_leave()
                temp_server = i
        temp_server.remove_job_from_queue(temp_job)
        return temp_job

    def handle_events(self):

        now = 0
        self.next_enter_event = 0

        while self.generated_jobs <= Main.entrance_number:
            temp_enter = self.get_next_enter_event(self.last_enter_event)
            temp_leave = self.get_next_leave_event()
            temp_process = self.get_next_process_event(now)

            if (temp_enter < temp_leave or Main.consider_drop is False) and temp_enter < temp_process:
                # Enter_Event
                now = temp_enter
                self.generated_jobs += 1
                self.add_new_process(now)
                self.next_enter_event = -1
            elif temp_leave < temp_enter and temp_leave < temp_process and Main.consider_drop is True:
                # Leave_Event
                now = temp_leave
                job = self.remove_leave_event_job()
                self.logger.add_log(job.forward_cost, job.enter_time, now, 'leaved')
            else:
                # Process_Event
                now = temp_process
                server = self.server_of_next_process
                job = server.get_next_job()
                server.remove_job_from_queue(job)
                self.logger.add_log(job.forward_cost, job.enter_time, now, 'served')
