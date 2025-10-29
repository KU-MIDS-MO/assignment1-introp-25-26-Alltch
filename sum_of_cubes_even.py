def sum_of_cubes_even(n):
    if not isinstance(n, int) or n < 0:
        return -1
    if n > 2000:
        return "warning but still compute"
    sum = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            sum += i * i * i
        else:
            continue
    return sum

print(sum_of_cubes_even(6))