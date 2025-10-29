def is_strictly_increasing_digits(n):
    if not isinstance(n, int) or n < 0:
        return -1
    if n < 10:
        return True
    digits = str(n)
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return False
    return True

print(is_strictly_increasing_digits(21))