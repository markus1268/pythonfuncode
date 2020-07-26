def fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#Memoization
def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

number = int(input("Masukkan bilangan n : "))
#print('Bilangan fibonacci {} : {}'.format(number, fibo(number)))
print('Bilangan fibonacci {} : {}'.format(number, fib(number)))
