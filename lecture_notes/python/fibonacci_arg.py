def fibonacci_robust(n):
    
    if (not isinstance(n, int)) or (n < 0):
        return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_robust(n-1) + fibonacci_robust(n-2)
    
    
import sys

print("This is the name of the program:",
       sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-1))
print("Argument List:",
       str(sys.argv))
