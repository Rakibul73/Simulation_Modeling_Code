c1 = [50.0]
c2 = [25.0]
c3 = [0.0]
kl = 0.025
k2 = 0.01
time_difference = 0.1
t = 0.0
last_time = 15.0
i = 0

print("\nTime  \tC1    \tC2    C3")

while t <= last_time:
    print(f"{t:.2f} \t{c1[i]:.2f} \t{c2[i]:.2f} \t{c3[i]:.2f}")

    c1_next = c1[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
    c2_next = c2[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
    c3_next = c3[i] + 2.0 * (kl * c1[i] * c2[i] - k2 * c3[i]) * time_difference

    c1.append(c1_next)
    c2.append(c2_next)
    c3.append(c3_next)

    i += 1
    t += time_difference

    if t >= 2.0:
        time_difference = 0.2
    if t == 6.0:
        time_difference = 0.4


