import sys

lines = iter(sys.stdin)

for a_line in lines:
    b_line = next(lines)

    a = int(a_line)
    b = int(b_line)

    print(a * b)
