# Рекурсивная мемоизированная функция пересчёта динамики.
#
# Мемоизация – «кэширование» (т.е. запоминание) результатов функции
# с целью использования, если они нам еще понадобятся

def fib_without_cache(n):  # не динамическое программирование
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib_without_cache(n-1) + fib_without_cache(n-2)

print(fib_without_cache(25))


## рекурсивная мемоизированная функция
#########33
from functools import lru_cache  ## => lru_cache => декоратор
# определяет вызывалась ли эта функция с аргументами, ли не вызывалась,
# если вызывалась, то берем результат функции с теми аргументами

# требуется больше памяти память
# быстрее скорость

@lru_cache(maxsize=None)
def fib_with_cache(n):  # не динамическое программирование
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib_with_cache(n-1) + fib_with_cache(n-2)


print(fib_with_cache(25))
print(fib_with_cache(500))
