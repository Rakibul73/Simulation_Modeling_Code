def mid_square(seed , num_random_num):
    result = []
    remove = int(len(str(seed))/2)
    
    for i in range(num_random_num):
        a = str(seed ** 2)
        middle = int((len(a)) / 2)
        r = a[middle - remove: middle + remove]
        seed = int(r)
        result.append(seed)
    return result


seed = int(input("Enter the seed: "))
num_random_num = int(input("Enter the number of random number you want: "))

random_numbers = mid_square(seed , num_random_num)
print("Generated random numbers:")
for num in random_numbers:
    print(num)
