A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Result matrix initialized with zeros
C = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for row in C:
    print(row)

#output:
Resultant Matrix:
[19, 22]
[43, 50]
