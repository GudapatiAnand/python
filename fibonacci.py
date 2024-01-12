#Python Progaram to solve the fibonacci sequence using recursion
#formula n=(n-1)+(n-2)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(3))