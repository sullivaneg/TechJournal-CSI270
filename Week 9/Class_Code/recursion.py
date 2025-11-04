#Source: https://www.pythonforbeginners.com/basics/fibonacci-series-in-python

def sumOfNumbers(N):
    if N == 1:
        return N
    else:
        return N + sumOfNumbers(N - 1)

num = int(input("Enter a number: "))
print(sumOfNumbers(num))
output = sumOfNumbers(num)
print("Sum of first {} natural numbers is {}".format(num, output))

#Fibonacci Series
fibonacciList = [0, 1]
# finding X terms of the series starting from 3rd term
X = int(input("Enter the number of terms to the series"))
term = 3
while term < X + 1:
    value = fibonacciList[term - 2] + fibonacciList[term - 3]
    fibonacciList.append(value)
    term = term + 1
print(X,"terms of the fibonacci series are:")
print(fibonacciList)