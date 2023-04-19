from functools import lru_cache

def fibonacci_direct(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):
   if n <= 1:
       return n
   else:
       return(fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

@lru_cache()
def fibonacci_memo(n):
    if n <= 1:
       return n
    else:
       return (fibonacci_memo(n-1) + fibonacci_memo(n-2))


if __name__ == '__main__':
    print('16th fibonacci number (recursive function): ', fibonacci_recursive(16))
    print('16th fiboncci number (memo function): ', fibonacci_memo(16))
    print('16th fibonacci number (direct function): ', fibonacci_direct(16))

r'''
C:\Users\blant\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/blant/PycharmProjects/pythonProject/venv/fib.py
16th fibonacci number (recursive function):  987
16th fiboncci number (memo function):  987
16th fibonacci number (direct function):  987

Process finished with exit code 0
'''