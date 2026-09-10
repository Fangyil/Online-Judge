import math


def prime_factors(n):
    count = 1
    exponent = 0

    # 處理質因數含2
    while n % 2 == 0:
        n //= 2
        exponent += 1
    count *= exponent + 1

    # 處理質因數為奇數
    factors = 3

    # 只需要嘗試到√n
    while factors * factors <= n:
        exponent = 0
        while n % factors == 0:
            n //= factors
            exponent += 1

        if exponent > 0:
            count *= exponent + 1

        factors += 2

    if n > 1:
        count *= 2

    return count


test_case = int(input())

for _ in range(test_case):
    lower, upper = map(int, input().split())

    divisors = 0
    product = lower
    for i in range(lower, upper + 1):
        tmp = prime_factors(i)
        if tmp > divisors:
            divisors = tmp
            product = i

    print(
        f"Between {lower} and {upper}, {product} has a maximum of {divisors} divisors."
    )
