def factorial(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n + 1):
        result += (-1)**i * x**(2*i+1) / factorial(2*i+1)
    print(f'{result}')
    
def approx_cos(x, n):
    result = 0
    for i in range(n + 1):
        result += (-1)**i * x**(2*i) / factorial(2*i)
    print(f'{result}')

def approx_sinh(x, n):
    result = 0
    for i in range(n + 1):
        result += x**(2*i+1) / factorial(2*i+1)
    print(f'{result}')
    
def approx_cosh(x, n):
    result = 0
    for i in range(n + 1):
        result += x**(2*i) / factorial(2*i)
    print(f'{result}')
    
if __name__ == '__main__':
    approx_sin(x = 3.14, n = 10)
    approx_cos(x = 3.14, n = 10)
    approx_sinh(x = 3.14, n = 10)
    approx_cosh(x = 3.14, n = 10)