# Обновляются все состояния, зависящие от текущего состояния.
N = 10
fib_numbers = [0] * N

fib_numbers[0] = 0  # Начальные значения
fib_numbers[1] = 1  # Начальные значения

for i in range(0, N):
    # Текущее i-e состояние оказывает влияние на i+1, i+2
    if i + 1 < N:
        fib_numbers[i + 1] = fib_numbers[i] + fib_numbers[i + 1]
    if i + 2 < N:
        fib_numbers[i + 2] += fib_numbers[i]

print(fib_numbers[-1])  # 10-е по порядку число Фибоначии 34