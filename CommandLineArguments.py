import sys
  
n = len(sys.argv)

for i in range(1, n):
    if(i==n-1):
        print(sys.argv[i], end = " ")
    else:
      print(sys.argv[i], '+', end = " ")

Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])
      
print("=", Sum)
