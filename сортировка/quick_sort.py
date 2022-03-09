import random

numbers = list(range(10))




def quick_sort(seq):
    # базовый случай
    if not seq:
        return []

    pivot = random.choice(seq)  # pivot -> опорный элемент из текущей последовательности
    left_part = [value for value in seq if value < pivot]  # пока не отсортирована (меньше опорного)
    right_part = [value for value in seq if value > pivot]  # пока не отсортирована (больше опорного)

    pivot_values = [value for value in seq if value == pivot]  # отсортировано(опорные элементы могут повторяться)

    return quick_sort(left_part) + pivot_values + quick_sort(right_part)

random.shuffle(numbers)  # shuffle -> перемешивает элементы
print(numbers)
sort_quick = quick_sort(numbers)
print(sort_quick)