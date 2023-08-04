def congruence_random_num(a, b, m, seed, num_of_random_numbers):
    random_nums = []
    current_num = seed

    for _ in range(num_of_random_numbers):
        current_num = (a * current_num + b) % m
        random_nums.append(current_num)

    return random_nums


a = int(input("Enter the value of 'a': "))
b = int(input("Enter the value of 'b': "))
m = int(input("Enter the value of 'm': "))
seed = int(input("Enter the seed value: "))
num_of_random_numbers = int(input("Enter the number of random numbers to generate: "))

random_numbers = congruence_random_num(a, b, m, seed, num_of_random_numbers)
print("Generated random numbers:")
for num in random_numbers:
    print(num)
