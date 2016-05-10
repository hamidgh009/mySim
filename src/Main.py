
from CostVector.CVGenerator import *
from Generators.Generator import *
from Logger.BaseLogger import *
from Logger.GraphLogger import *
from ServerChooser.ServerChooser import *
from Graph.BaseGraph import *
from GraphEventHandler import *
from EventHandler import *

number_of_servers = 200
server_buffer_size = 80

min_cost_dist = 'random'
vector_dist = 'simple'

enter_dist = 'poisson'
enter_lambda = 200

job_limit_dist = 'poisson'
job_limit_lambda = 0.1
consider_drop = False

job_process_time_dist = 'fix'
job_process_time_lambda = 1

time_unit = 1000

entrance_number = 100000

# graph model parameters
sample_rate = 0.001
p = 0.5
i = 3


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


def create_generator(landa, distribution):
    if distribution == 'poisson':
        return ExponentialGenerator(landa, time_unit)
    elif distribution == 'fix':
        return FixedGenerator(landa, time_unit)
    else:
        return ConstantGenerator(landa, time_unit)


def run_nth_best():
    logger = BaseLogger()
    for x in my_range(2, number_of_servers, 1):
        entrance_gen = create_generator(enter_lambda, enter_dist)
        limit_gen = create_generator(job_limit_lambda, job_limit_dist)
        process_gen = create_generator(job_process_time_lambda, job_process_time_dist)
        server_chooser = NthBestServerChooser(x)
        cv_gen = LinearCVGenerator(number_of_servers, 0, 1)
        handler = EventHandler(logger, entrance_gen, limit_gen, process_gen, cv_gen, server_chooser)
        handler.handle_events()
        logger.calculate_ehtemalat(x, entrance_number)
        logger.calculate_cost_waiting(x)
        logger.reset()
        print x
    logger.draw_cost_waiting_time()


def run_simple():
    logger = BaseLogger()
    for x in my_range(0.2, 20, 0.1):
        entrance_gen = create_generator(x, enter_dist)
        limit_gen = create_generator(job_limit_lambda, job_limit_dist)
        process_gen = create_generator(job_process_time_lambda, job_process_time_dist)
        server_chooser = ServerChooser()
        cv_gen = LinearCVGenerator(number_of_servers, 0, 1)
        handler = EventHandler(logger, entrance_gen, limit_gen, process_gen, cv_gen, server_chooser)
        handler.handle_events()
        logger.calculate_ehtemalat(x, entrance_number)
        logger.reset()
        print x

    logger.draw_served_probability()
    logger.draw_blocked_probability()
    logger.draw_leaved_probability()


def run_graph_mode():
    graph = BaseGraph(number_of_servers, p)
    print graph.get_number_of_edges()
    logger = GraphLogger(graph, sample_rate, i)
    entrance_gen = create_generator(enter_lambda, enter_dist)
    limit_gen = create_generator(job_limit_lambda, job_limit_dist)
    process_gen = create_generator(job_process_time_lambda, job_process_time_dist)
    server_chooser = GraphChooser(graph)
    cv_gen = LinearCVGenerator(number_of_servers, 0, 1)
    handler = GraphEventHandler(logger, entrance_gen, limit_gen, process_gen, cv_gen, server_chooser)
    handler.handle_events()
    logger.draw_samples_graph1(p)
    logger.draw_samples_graph2(p)

if __name__ == '__main__':
    # run_nth_best()
    run_graph_mode()

