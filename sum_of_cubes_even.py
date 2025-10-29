def sum_of_cubes_even(n):
    if not isinstance(n, int) or n < 0:
        return -1
    if n > 2000:
        print("warning: but still compute")
    total = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            total += i ** 3
    return float(total)

print(sum_of_cubes_even(6))