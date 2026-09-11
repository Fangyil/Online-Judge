def around(results, x, y, n, m):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < n and 0 <= j < m:
                if results[i][j] != "*":
                    results[i][j] += 1


cases = 0
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    cases += 1
    maps = []
    for _ in range(n):
        maps.append(input())

    results = [[0] * (m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "*":
                results[i][j] = "*"
                around(results, i, j, n, m)

    if cases > 1:
        print()

    print(f"Field #{cases}:")

    for row in results:
        print("".join(map(str, row)))
