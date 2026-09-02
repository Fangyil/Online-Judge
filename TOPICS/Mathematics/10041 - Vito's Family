def cal_dist(vito, streets):
    return sum(abs(vito - street) for street in streets)


test_cases = int(input())

for _ in range(test_cases):

    data = list(map(int, input().split()))
    relatives = data[0]
    street = data[1:]

    ## 找中位數時，先排序再取中間位數
    street.sort()
    median = street[len(street) // 2]

    print(cal_dist(median, street))

    #################################################
    ### 以平均值當 Vito's house 時，離群值會嚴重影響計算###
    #################################################
    # total = sum(street)
    # vito_down = total // relatives
    # vito_up = vito_down + 1

    # distance_down = cal_dist(vito_down, street)

    # if total % relatives == 0:
    #     print(distance_down)
    # else:
    #     distance_up = cal_dist(vito_up, street)
    #     print(min(distance_down, distance_up))
