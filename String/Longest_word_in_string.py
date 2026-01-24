s = input("Enter a string: ")

words = s.split()
print(max(words, key=len))

#output:
Enter a string: Python programming is fun
programming
