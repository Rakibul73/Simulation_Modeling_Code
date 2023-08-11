import random
import simpy

RANDOM_SEED = 42
SIM_TIME = 1000
SERVICE_TIME = 5

class SingleServerQueue:
    def __init__(self, env, service_time): 
        self.server = simpy.Resource(env, capacity=1)
        self.service_time = service_time
    def service(self):
        yield env.timeout (random.expovariate(1/self.service_time))

def customer_arrivals(env, queue):
    i = 0
    while True:
        i += 1 
        yield env.timeout(random.expovariate(1/5)) 
        env.process(customer (env, f'Customer {i}', queue))

def customer(env, name, queue): 
    print (f" {env.now}: {name} arrived")
    with queue.server.request() as request:
        yield request
        print(f" {env.now}: {name} being served")
        yield env.process(queue.service())
        print(f"{env.now}: {name} finished being served")

# Setup and start the simulation 
random.seed(RANDOM_SEED)
env = simpy.Environment()
queue = SingleServerQueue(env, SERVICE_TIME) 
env.process(customer_arrivals (env, queue))
env.run(until=SIM_TIME)