import random

SEED = 12345

def main():
    week = 1
    t = [0] * 10
    count = 0
    kont = 0
    clock = 0
    run = 20000
    cost1 = 0
    cost2 = 0

    random.seed(SEED)

    # Present policy
    for i in range(1, 5):
        x = random.random()
        x = (round(x , 6))
        print(x , end=" ")
        t[i] = int(1000 + x * 1000)
        print(f"{t[i]:>8}", end="\n")

    print("\n CLOCK T1 T2 T3 T4 COUNT")

    while clock <= run:
        print(f"\n {clock:>5} {t[1]:>5} {t[2]:>5} {t[3]:>5} {t[4]:>5} {count:>5}")

        small = 999999
        jj = 0
        for i in range(1, 5):
            if t[i] < small:
                small = t[i]
                jj = i

        for i in range(1, 5):
            t[i] -= small

        x = random.random()
        x = round(x, 6)
        t[jj] = int(1000 + x * 1000)
        clock += small
        count += 1

    # Proposed policy
    clock = 0
    kont = 0
    random.seed(SEED)

    print("\n CLOCK TI T2 T3 T4 KONT")

    while clock <= run:
        for i in range(1, 5):
            x = random.random()
            x = round(x, 6)
            t[i] = int(1000 + x * 1000)

        print(f"\n {clock:>5} {t[1]:>5} {t[2]:>5} {t[3]:>5} {t[4]:>5} {kont:>5}")

        small = 999999
        for i in range(1, 5):
            if t[i] < small:
                small = t[i]

        clock += small
        kont += 1

    cost1 = count * (200 + 100)
    cost2 = kont * 2 * 200 + kont * 4 * 100

    print(f"\nCost Present policy  = {cost1}\nCost proposed policy = {cost2}")

if __name__ == "__main__":
    main()
