import simpy
import random
import matplotlib.pyplot as plt

class SingleServerQueue:
    def __init__(self, env, arrival_rate, service_rate):
        self.env = env
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.queue_length = 0
        self.waiting_times = []

    def customer_arrival(self):
        while True:
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            self.queue_length += 1
            self.env.process(self.customer_service(self.env.now))  # Capture arrival time

    def customer_service(self, arrival_time):
        service_time = random.expovariate(self.service_rate)
        yield self.env.timeout(service_time)
        departure_time = self.env.now
        self.queue_length -= 1
        waiting_time = departure_time - arrival_time
        self.waiting_times.append(waiting_time)

if __name__ == '__main__':
    arrival_rate = 0.5  # Average arrival rate of customers per unit of time
    service_rate = 0.6  # Average service rate of the server per unit of time
    simulation_time = 1000

    env = simpy.Environment()
    queue_system = SingleServerQueue(env, arrival_rate, service_rate)
    env.process(queue_system.customer_arrival())
    env.run(until=simulation_time)

    # Calculate and print average waiting time
    average_waiting_time = sum(queue_system.waiting_times) / len(queue_system.waiting_times)
    print("Average Waiting Time:", average_waiting_time)

    # Plotting the waiting time distribution
    plt.hist(queue_system.waiting_times, bins=30, density=True, alpha=0.7, color='blue')
    plt.xlabel('Waiting Time')
    plt.ylabel('Probability Density')
    plt.title('Waiting Time Distribution in Single-Server Queuing System')
    plt.show()
