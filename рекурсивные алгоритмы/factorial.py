def factorial(n):
    f = 1

    for i in range(1, n + 1):
        f *= i
        print(f)
    return f


print(factorial(5))

# LIFO => LAST IN FIRST OUT
def factorial(n: int) -> int:
    if n == 0:
        return 1  # базовый случай, не нужно вычислять с помощью рекурсии
    return factorial(n - 1) * n  # рекуретная формул


print(factorial(5))
