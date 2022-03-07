# Мальчик подошел к платной лестнице.
# Чтобы наступить на ступенку, нужно заплатить сумму, на ней указанную
# (не обязательно номер ступеньки).
# Мальчик умеет шагать на одну ступеньку или через одну.
#
# Вопрос: какая наименьшая сумма понадобится мальчику
# для достижения верхней ступеньки?
#
# stair_coasts = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3, 0, 0]  # 2**N   # стоимость наступить на каждую ступеньку
#
# stair_total_coasts = [float("+inf")] * (len(stair_coasts) - 2)
# for stair_index in range(len(stair_coasts)):
#     stair_total_coasts[stair_index + 1] = min(
#         stair_total_coasts[stair_index + 1],
#         stair_total_coasts[stair_index] + stair_coasts[stair_index+1]
#     )
#     stair_total_coasts[stair_index + 2] = min(
#         stair_total_coasts[stair_index + 2],
#         stair_total_coasts[stair_index] + stair_coasts[stair_index+1]
#     )
#
# print(stair_total_coasts[-1])





################ ленивый метод обхода
stair_coasts = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]  # 2**N   # стоимость наступить на каждую ступеньку
total_coast = []
count_stair = len(stair_coasts)
def get_coast(n):
    if n == 1:
        return stair_coasts[n-1]

    if n == 2:
        # return stair_coasts[n-1]
        return min(
            stair_coasts[n-1],  # дешевле наступить сразу на 2 ступень или
            stair_coasts[n-1] + stair_coasts[n-2]  # дешевле сначала на первую потом на вторую
        )

    current_stair = stair_coasts[n-1]  # стоимость текущей ступени

    return current_stair + min(get_coast(n-1),
                               get_coast(n-2))

print(get_coast(count_stair))