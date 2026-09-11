import sys
import math

for line in sys.stdin:
    print(line.strip() + "!")
    print(math.factorial(int(line)))
