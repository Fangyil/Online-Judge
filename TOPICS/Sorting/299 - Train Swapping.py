test_cases = int(input())

for _ in range(test_cases):
    train_length = int(input())
    train = list(map(int,input().split()))

    exchange = 0
    #只需要計算左邊有多少數比自己大即可
    for i in range(len(train)):
        for j in range(i):
            if train[j] > train[i]:
                exchange += 1

    print(f"Optimal train swapping takes {exchange} swaps.")
