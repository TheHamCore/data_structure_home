def fibonachi(num):
    # F0 = 0, F1 = 1
    if num in (1, 2):
        return 1

    # Fn=Fn−1+Fn−2,n≥ 2
    return fibonachi(num - 1) + fibonachi(num - 2)


print(fibonachi(10))


# итеративный алгоритм фибоначи

def iter_fib():  # возвращает следующее значение
    """возвращает текущее число фибонначи"""
    a = 0
    yield a

    b = 1
    yield b

    while True:
        a, b = b, a + b
        yield b


my_iter_fib = iter_fib(10)
for _ in range(10):  # O(n)
    print(next(my_iter_fib))

#######################################################################################################
def iter_fib_n(n):  # возвращает следующее значение
    """возвращает текущее число фибонначи"""
    a = 0

    b = 1

    for _ in range(n):
        a, b = b, a + b
    return b

print(iter_fib_n(10))