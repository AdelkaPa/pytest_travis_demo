def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError("n is not an int")
    if n <= 0:
        raise ValueError("n is not positive")
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    if n % 15 == 0:
        return 'fizzbuzz'
    return str(n)
    


