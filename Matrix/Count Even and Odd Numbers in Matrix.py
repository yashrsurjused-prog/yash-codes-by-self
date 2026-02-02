matrix = [[1, 2], [3, 4]]
even = 0
odd = 0

for row in matrix:
    for item in row:
        if item % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even:", even)
print("Odd:", odd)

#Output:
Even: 2
Odd: 2
