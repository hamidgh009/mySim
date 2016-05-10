from EventHandler import EventHandler
import Job


class GraphEventHandler(EventHandler):

    def add_new_process(self, now):
        self.server_chooser.set_decision_pars(self.servers)
        server_number = self.server_chooser.choose_server(None)
        temp_job = Job.Job(now, self.limit_time_generator.generate(),
                           self.process_time_generator.generate(), 0)
        added = self.servers[server_number].add_new_job(temp_job)
        if not added:
            self.logger.add_log(temp_job.forward_cost, temp_job.enter_time, temp_job.enter_time, 'blocked')
        self.logger.add_sample(self.servers)
        return
