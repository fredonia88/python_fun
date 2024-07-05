def string_reversal(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + string_reversal(s[:-1])

def palindrome_check(s: str) -> bool:

    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindrome_check(s[1:-1])

def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n-1)

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(n: int) -> int:
    if n < 10:
        return n 
    return n % 10 + sum_of_digits(n // 10)

def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return a % b # throw error
    elif b == 0:
        return a
    
    return gcd(b, a % b)

def tower_of_hanoi(discs: int, source: str='Tower1', helper: str='Tower2', destination: str='Tower3') -> str:
    if discs == 1:
        print(f'Moving disc 1 from {source} to {destination}')
        return 
    tower_of_hanoi(discs-1, source, destination, helper)
    print(f'Moving disc {discs} from {source} to {destination}')
    tower_of_hanoi(discs-1, helper, source, destination)
