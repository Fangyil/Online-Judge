import sys

for line in sys.stdin:
    state = 0

    data = list(map(int, line.split()))
    n = data[0]
    diff = [0] * n
    for i in range(2, n + 1):

        tmp = abs(data[i] - data[i - 1])
        if tmp < 1 or tmp > n - 1:
            state = 1
            break

        diff[tmp] += 1
        if diff[tmp] > 1:
            state = 1
            break

    if state:
        print("Not jolly")
    else:
        print("Jolly")
