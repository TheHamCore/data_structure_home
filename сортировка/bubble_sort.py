import random


def bubble_sort(seq):
    """Сортируем по убыванию -> от большего к меньшему"""
    for _ in range(len(seq)):  # O(N)
        for i in range(len(seq) - 1):  # O(N)
            # сравниваю i и i+1  // красные квадраты из лекции
            if seq[i] < seq[i + 1]:  # элемент легче
                seq[i], seq[i + 1] = seq[i + 1], seq[i]

    print(seq)  # [124, 23, 21, 17, 12, 2, 2, 1]
    # O(n**2)


bubble_sort([1, 23, 124, 2, 2, 21, 17, 12])

