numbersList = [1, 5, 4, 6, 8, 11, 3, 12]

evenNumbers = list(filter(lambda n: (n%2 == 0), numbersList))

print(evenNumbers)

oddNumbers = list(filter(lambda n: (n%2 != 0), numbersList))

print(oddNumbers)