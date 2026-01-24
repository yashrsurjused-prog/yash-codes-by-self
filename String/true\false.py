s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s3 = input("Enter third string: ")

print(s1.isalnum())   # letters + numbers
print(s2.isdigit())   # digits only
print(s3.isalpha())   # alphabets only
print(s3.islower())   # lowercase
print(s3.isupper())   # uppercase

#output:
Enter first string: Python123
Enter second string: 123
Enter third string: python
True
True
True
True
False
