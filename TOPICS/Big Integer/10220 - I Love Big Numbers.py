import sys
import math

for line in sys.stdin:
    ans = 0
    num = math.factorial(int(line))

    while num != 0:
        ans += num % 10
        num //= 10

    print(ans)
