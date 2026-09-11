import sys


def lcs_length(a, b):
    m = len(a)
    n = len(b)
    common = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                common[i][j] = common[i - 1][j - 1] + 1
            elif common[i - 1][j] >= common[i][j - 1]:
                common[i][j] = common[i - 1][j]
            else:
                common[i][j] = common[i][j - 1]

    return common


case_number = 0
while True:
    case_a, case_b = map(int, input().split())

    if case_a == 0 and case_b == 0:
        break

    case_number += 1
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    common = lcs_length(a, b)

    print(f"Twin Towers #{case_number}")
    print(f"Number of Tiles : {common[-1][-1]}\n")
