import random


# inplace
# доп память
def bubble_sort_2(seq):
    """Сортируем по убыванию -> от большего к меньшему"""
    for _ in range(len(seq)):  # O(N)
        for i in range(1, len(seq)):  # O(N)
            if seq[i - 1] < seq[i]:
                seq[i - 1], seq[i] = seq[i], seq[i - 1]

    return seq

# думаем, на что может проверить => тестовые случаи


src_seq = list(range(100))
dst_seq = list(range(99, -1, -1))  # list(reversed(src_seq)


# по возрастанию
assert bubble_sort_2(src_seq) == dst_seq


# по убыванию
src_seq = list(range(100, -1, -1))
assert bubble_sort_2(src_seq) == src_seq

# случайные элементы
src_seq = list(range(100))
dst_seq = list(reversed(src_seq))
random.shuffle(src_seq)
assert bubble_sort_2(src_seq) == dst_seq

# пустая последовательность
assert bubble_sort_2([]) == []


# из 1 элемента
assert bubble_sort_2([1]) == [1]
# из 2 элемента
assert bubble_sort_2([1, 2]) == [2, 1]
# все одинаковые
# все уникальные


# numbers = [1, 2, 3, 4]
# assert random.shuffle(numbers)

# assert 1 == 1  # если True, ok
# assert 1 == 2  # если False, то Exceptiom
# print(seq)  # [124, 23, 21, 17, 12, 2, 2, 1]
# # O(n**2)
