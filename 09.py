def is_prime(num):
    count = 0
    for n in range(1, num + 1):
        if num % n == 0:
            count += 1
    return count == 2

def Prime_time(n):
    result = []
    for num in range(1, n + 1):
        if is_prime(num):
            result.append(num)
    return result

print(Prime_time(11))
print(Prime_time(7))
print(Prime_time(13))