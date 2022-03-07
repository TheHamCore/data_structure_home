some_seq = [x for x in range(10)]  # index 0 .... len - 1


def recursion_binary_search(seq, search_value,
                            left_border=None, right_border=None) -> int:
    """Функция возвращает индекс найденного элемента либо None
    - ** Левосторонний поиск или правосторонний
    return index
    """
    if left_border is None:
        left_border = 0
    if right_border is None:
        right_border = len(seq) - 1

    if left_border > right_border:
        return None  # если элемента не было


    middle = (left_border + right_border) // 2  # не важно вправо или влево

    middle_value = seq[middle]
    if middle_value == search_value:
        return middle

    elif middle_value < search_value:  # идём в правую половину
        new_left_border = middle_value + 1
        return recursion_binary_search(seq, search_value, new_left_border, right_border)  # todo не забыть вернуть индекс

    elif middle_value > search_value:  # идем в левую половину
        new_right_border = middle_value - 1
        return recursion_binary_search(seq, search_value, left_border, new_right_border)


print(recursion_binary_search(some_seq, 5))
print(recursion_binary_search(some_seq, 5))