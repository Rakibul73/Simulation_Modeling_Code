/* External definitions for inventory system. */
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "lcgrand.h" /* Header file for random-number generator. */

int amount, bigs, initial_inv_level, inv_level, next_event_type, num_events,
    num_months, num_values_demand, smalls;
float area_holding, area_shortage, holding_cost, incremental_cost, maxlag,
    mean_interdemand, minlag, prob_distrib_demand[26], setup_cost,
    shortage_cost, sim_time, time_last_event, time_next_event[5],
    total_ordering_cost;

void initialize(void);
void timing(void);
void order_arrival(void);
void demand(void);
void evaluate(void);
void report(void);
void update_time_avg_stats(void);
float expon(float mean);
int random_integer(float prob_distrib[]);
float uniform(float a, float b);

int main() /* Main function. */
{
    int i, num_policies;

    /* Specify the number of events for the timing function. */
    num_events = 4;

    /* Read input parameters. */
    scanf("%d %d %d %d %f %f %f %f %f %f %f",
           &initial_inv_level, &num_months, &num_policies, &num_values_demand,
           &mean_interdemand, &setup_cost, &incremental_cost, &holding_cost,
           &shortage_cost, &minlag, &maxlag);

    for (i = 1; i <= num_values_demand; ++i)
        scanf("%f", &prob_distrib_demand[i]);

    /* Print report heading and input parameters. */
    printf("Single-product inventory system\n\n");
    printf("Initial inventory level%24d items\n\n",
            initial_inv_level);
    printf("Number of demand sizes%25d\n\n", num_values_demand);
    printf("Distribution function of demand sizes ");
    for (i = 1; i <= num_values_demand; ++i)
        printf("%8.3f", prob_distrib_demand[i]);
    printf("\n\nMean interdemand time%26.2f\n\n", mean_interdemand);
    printf("Delivery lag range%29.2f to%10.2f months\n\n", minlag,
            maxlag);
    printf("Length of the simulation%23d months\n\n", num_months);
    printf("K =%6.1f i =%6.1f h =%6.1f pi =%6.1f\n\n",
            setup_cost, incremental_cost, holding_cost, shortage_cost);
    printf("Number of policies%29d\n\n", num_policies);

    // Print input prompts and read the inventory policy pairs
    printf("Enter inventory policy pairs (smalls bigs) for each policy:\n");
    int smalls_arr[10]; // Assuming at most 10 policies
    int bigs_arr[10];   // Assuming at most 10 policies

    for (int i = 0; i < num_policies; ++i)
    {
        scanf("%d %d", &smalls_arr[i], &bigs_arr[i]);
    }

    printf("Policy\tAverage total cost\tAverage ordering cost\t");
    printf("Average holding cost\tAverage shortage cost\n");


    /* Run the simulation varying the inventory policy. */
    for (i = 0; i < num_policies; ++i)
    {
        /* Read the inventory policy, and initialize the simulation. */
        smalls = smalls_arr[i];
        bigs = bigs_arr[i];
        initialize();

        /* Run the simulation until it terminates after an end-simulation event
        (type 3) occurs. */
        do
        {
            /* Determine the next event. */
            timing();

            /* Update time-average statistical accumulators. */
            update_time_avg_stats();

            /* Invoke the appropriate event function. */
            switch (next_event_type)
            {
            case 1:
                order_arrival();
                break;
            case 2:
                demand();
                break;
            case 4:
                evaluate();
                break;
            case 3:
                report();
                break;
            }
        } while (next_event_type != 3);
    }

    return 0;
}

void report(void) /* Report generator function. */
{
    /* Compute and display estimates of desired measures of performance. */
    float avg_holding_cost, avg_ordering_cost, avg_shortage_cost;
    avg_ordering_cost = total_ordering_cost / num_months;
    avg_holding_cost = holding_cost * area_holding / num_months;
    avg_shortage_cost = shortage_cost * area_shortage / num_months;
    
    printf("\n\n(%3d,%3d)%15.2f%15.2f%15.2f%15.2f",
            smalls, bigs,
            avg_ordering_cost + avg_holding_cost + avg_shortage_cost,
            avg_ordering_cost, avg_holding_cost, avg_shortage_cost);
}
void initialize(void) /* Initialization function. */
{
    /* Initialize the simulation clock. */
    sim_time = 0.0;
    /* Initialize the state variables. */
    inv_level = initial_inv_level;
    time_last_event = 0.0;
    /* Initialize the statistical counters. */
    total_ordering_cost = 0.0;
    area_holding = 0.0;
    area_shortage = 0.0;
    /* Initialize the event list. Since no order is outstanding, the order-
    arrival event is eliminated from consideration. */
    time_next_event[1] = 1.0e+30;
    time_next_event[2] = sim_time + expon(mean_interdemand);
    time_next_event[3] = num_months;
    time_next_event[4] = 0.0;
}
void order_arrival(void) /* Order arrival event function. */
{
    /* Increment the inventory level by the amount ordered. */
    inv_level += amount;
    /* Since no order is now outstanding, eliminate the order-arrival event from
    consideration. */
    time_next_event[1] = 1.0e+30;
}
void demand(void) /* Demand event function. */
{
    /* Decrement the inventory level by a generated demand size. */
    inv_level -= random_integer(prob_distrib_demand);
    /* Schedule the time of the next demand. */
    time_next_event[2] = sim_time + expon(mean_interdemand);
}
void evaluate(void) /* Inventory-evaluation event function. */
{
    /* Check whether the inventory level is less than smalls. */
    if (inv_level < smalls)
    {
        /* The inventory level is less than smalls, so place an order for the
        appropriate amount. */
        amount = bigs - inv_level;
        total_ordering_cost += setup_cost + incremental_cost * amount;
        /* Schedule the arrival of the order. */
        time_next_event[1] = sim_time + uniform(minlag, maxlag);
    }
    /* Regardless of the place-order decision, schedule the next inventory
    evaluation. */
    time_next_event[4] = sim_time + 1.0;
}



void update_time_avg_stats(void) /* Update area accumulators for time-average statistics. */
{
    float time_since_last_event;
    /* Compute time since last event, and update last-event-time marker. */
    time_since_last_event = sim_time - time_last_event;
    time_last_event = sim_time;
    /* Determine the status of the inventory level during the previous interval.
    If the inventory level during the previous interval was negative, update
    area_shortage. If it was positive, update area_holding. If it was zero,
    no update is needed. */
    if (inv_level < 0)
        area_shortage -= inv_level * time_since_last_event;
    else if (inv_level > 0)
        area_holding += inv_level * time_since_last_event;
}
int random_integer(float prob_distrib[]) /* Random integer generation
 function. */
{
    int i;
    float u;
    /* Generate a U(0,1) random variate. */
    u = lcgrand(1);
    /* Return a random integer in accordance with the (cumulative) distribution
    function prob_distrib. */
    for (i = 1; u >= prob_distrib[i]; ++i)
        ;
    return i;
}
float uniform(float a, float b) /* Uniform variate generation function. */
{
    /* Return a U(a,b) random variate. */
    return a + lcgrand(1) * (b - a);
}
void timing(void) /* Timing function. */
{
    int i;
    float min_time_next_event = 1.0e+29;
    next_event_type = 0;
    /* Determine the event type of the next event to occur. */
    for (i = 1; i <= num_events; ++i)
    {
        if (time_next_event[i] < min_time_next_event)
        {
            min_time_next_event = time_next_event[i];
            next_event_type = i;
        }
    }
    /* Check to see whether the event list is empty. */
    if (next_event_type == 0)
    {
        /* The event list is empty, so stop the simulation. */
        printf("\nEvent list empty at time %f", sim_time);
        exit(1);
    }
    /* The event list is not empty, so advance the simulation clock. */
    sim_time = min_time_next_event;
}

float expon(float mean) /* Exponential variate generation function. */
{
    /* Return an exponential random variate with mean "mean". */
    return -mean * log(lcgrand(1));
}