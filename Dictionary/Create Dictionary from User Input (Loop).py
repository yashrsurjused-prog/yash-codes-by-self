n = int(input("How many entries: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print(data)

#Input:
2
name
Yash
age
19
#Output:
{'name': 'Yash', 'age': '19'}
