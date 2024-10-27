def fibonnaci_sequence_generator(n):  
    sequence = [0, 1]
    a = sequence[0]
    b = sequence[1]
    
    for i in range(n - 2):
        c = a + b
        sequence.append(c)
        a = b
        b = c
    return sequence

print(fibonnaci_sequence_generator(5))
print(fibonnaci_sequence_generator(7))