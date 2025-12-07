 #2.	Write a recursive function that generates nth Fibonacci number.
# Test your code by generating 100th Fibonacci number.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Working Test Case
print(fibonacci(20))

# Test Case
#for n in range(101):
    #print(fibonacci(n))

#import timeit
#for n in range(101):
    #num = timeit.timeit("fibonacci(n)", setup="from __main__ import fibonacci, n", number=1)
    ##print("n =", n, "| Fibonacci number:", num2, "| Time:", num)