import sys
import math


def space(state):
    return state // 8, state % 8


for line in sys.stdin:
    data = list(map(int, line.split()))

    king_state = data[0]
    queen_state = data[1]
    new_queen_state = data[2]

    if queen_state == king_state:
        print("Illegal state")
        continue

    if new_queen_state == king_state or new_queen_state == queen_state:
        print("Illegal move")
        continue

    row_king, column_king = space(king_state)
    row_queen, column_queen = space(queen_state)
    row_new_queen, column_new_queen = space(new_queen_state)

    if row_new_queen != row_queen and column_new_queen != column_queen:
        print("Illegal move")

    elif (
        row_new_queen == row_king
        and row_new_queen == row_queen
        and (
            column_new_queen < column_king < column_queen
            or column_new_queen > column_king > column_queen
        )
    ) or (
        column_new_queen == column_king
        and column_new_queen == column_queen
        and (
            row_new_queen < row_king < row_queen or row_new_queen > row_king > row_queen
        )
    ):
        print("Illegal move")

    elif (column_new_queen == column_king and abs(row_new_queen - row_king) == 1) or (
        row_new_queen == row_king and abs(column_new_queen - column_king) == 1
    ):
        print("Move not allowed")

    elif (
        (king_state == 0 and new_queen_state == 9)
        or (king_state == 7 and new_queen_state == 14)
        or (king_state == 56 and new_queen_state == 49)
        or (king_state == 63 and new_queen_state == 54)
    ):
        print("Stop")

    else:
        print("Continue")
