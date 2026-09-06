test_case = int(input())

for _ in range(test_case):
    day = int(input()) + 1
    works = [0] * day
    party = int(input())
    for _ in range(party):
        hartal = int(input())

        # original 經過每一天來幾計算有沒有碰到 hartal
        # for i in range(day):
        #     if i % hartal == 0 and i % 7 != 0 and i % 7 != 6:
        #         works[i] = 1

        # 只尋找 hartal 有沒有碰到罷工
        for i in range(hartal, day, hartal):
            if i % 7 != 0 and i % 7 != 6:
                works[i] = 1

    print(sum(works))
