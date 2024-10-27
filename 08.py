def orders(s):
    s = s.split(" ")
    result = []

    for position in range(len(s) + 1):
        for word in s:
            if str(position) in word:
                result.append(word)
    return " ".join(result)

print(orders("is2 Thi1s T4est 3a"))
print(orders("4of Fo1r pe6ople g3ood th5e the2"))
print(orders(""))