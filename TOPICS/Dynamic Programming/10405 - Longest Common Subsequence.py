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


lines = iter(sys.stdin)

for a_line in lines:
    b_line = next(lines)
    a = a_line.rstrip("\n")
    b = b_line.rstrip("\n")

    common = lcs_length(a, b)

    print(common[len(a)][len(b)])
