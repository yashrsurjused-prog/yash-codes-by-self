people = {
    "Yash": 19,
    "Amit": 22,
    "Neha": 20
}

oldest = max(people, key=people.get)

print("Oldest:", oldest)

#Output:
Oldest: Amit
