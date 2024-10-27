def remove_dublicates(lst):
    result = []
    for element in lst:
        if element not in result:
            result.append(element)
    return result

print(remove_dublicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_dublicates(['a', 'b', 'a', 'c']))