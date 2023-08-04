import random

print("\nwait , program in running .........")

def play_game():
    lose_money = 0
    head_count = 0
    tail_count = 0
    # print("." , end=" ")
    
    while abs(head_count - tail_count) < 3:
        lose_money += 1
        if random.randint(0, 9) < 5:
            head_count += 1
        else:
            tail_count += 1

    return lose_money

n_simulations = 1000000
total_lose_money = sum(play_game() for _ in range(n_simulations))
total_gain_money = n_simulations*8
expected_outcome = total_lose_money / n_simulations

print("\nEach game on the average requires", expected_outcome , "Flips for simulation")
print("Each game on the average requires 9 Flips in truly")
