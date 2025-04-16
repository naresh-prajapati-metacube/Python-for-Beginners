#  Iterating through a string Using List Comprehension
lettersArr = [ letter for letter in 'human' ]
print( lettersArr)

# Using Lambda functions inside List
lettersArr = list(map(lambda l:l, 'human'))
print(lettersArr)


# Conditionals in List Comprehension
numbersArr = [x for x in range(20) if (x%2 != 0)]
print(numbersArr)

# Nested IF with List Comprehension
numbersArr = [x for x in range(40) if (x%3==0) if (x%5==0)]
print(numbersArr)

#  if...else With List Comprehension
evenOddArr = ['Even' if (i%2==0) else 'Odd' for i in range(20)]
print(evenOddArr)

# Transpose of Matrix using Nested Loops
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposedArr = []
for i in range(len(matrix[0])):
    rowArr = []
    for row in matrix:
        rowArr.append(row[i])
    transposedArr.append(rowArr)
print(transposedArr)

# Transpose of a Matrix using List Comprehension
transposedArr = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposedArr)