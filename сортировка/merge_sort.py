def merge_func(left, right):
    """Функция слияния отсортированных кусков"""

    ...


def merge_sort(seq):
    if len(seq) == 1:
        return seq

    middle_index = len(seq) // 2

    return merge_func(
        merge_sort(seq[:middle_index]),  # сортируем левую часть
        merge_sort(seq[middle_index:]),  # сортируем правую часть
    )
