def calculate(number):
    if not isinstance(number,(int,float)):
        raise TypeError("Temperature must be a numeric value.")
    number1=(number-32)*5.0/9.0
    return number1

def fibonacci(n):
    if not isinstance(n,int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)