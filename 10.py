def is_eureka(n):
    result = 0
    power = 1
    for digit in str(n):
        result += int(digit) ** power
        power += 1
    return result == n

def eureka_nums(n1, n2):
    result = []
    for num in range(n1, n2):
        if is_eureka(num):
            result.append(num)
    return result

print(eureka_nums(1, 10))
print(eureka_nums(1, 100))