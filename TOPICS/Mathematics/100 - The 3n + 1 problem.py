# sys處理多筆測資，cache儲存數據降低重複計算
import sys

cache = {1: 1}


def cycle_length(n):
    original = n
    path = []
    while n not in cache:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    count = cache[n]

    for value in reversed(path):
        count += 1
        cache[value] = count
    return cache[original]


for line in sys.stdin:
    if not line.strip():
        continue

    a, b = map(int, line.split())
    start = min(a, b)
    end = max(a, b)

    max_count = 0

    for number in range(start, end + 1):
        count = cycle_length(number)

        if count > max_count:
            max_count = count

    print(a, b, max_count)
