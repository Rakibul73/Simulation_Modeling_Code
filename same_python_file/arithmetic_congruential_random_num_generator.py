def arithmetic_congruential_generator(seed1, seed2, m, num_of_random_numbers):
    random_nums = []
    num1, num2 = seed1, seed2

    for _ in range(num_of_random_numbers):
        new_num = (num1 + num2) % m
        random_nums.append(new_num)
        num1, num2 = num2, new_num

    return random_nums


seed1 = int(input("Enter the first seed value: "))
seed2 = int(input("Enter the second seed value: "))
m = int(input("Enter the value of 'm' (should largest prime num): "))
num_of_random_numbers = int(input("Enter the number of random numbers to generate: "))

random_numbers = arithmetic_congruential_generator(seed1, seed2, m, num_of_random_numbers)
print("Generated random numbers:")
for num in random_numbers:
    print(num)
