def count_digits_greater_than(n, t):
    if not isinstance(n, int) or not isinstance(t, int):
        return -1
    if n < 0 or t < 0 or t > 9:
        return -1
    count = 0
    for digit in str(n):
        if int(digit) > t:
            count += 1
    return count


print(count_digits_greater_than(65222211114, 3))