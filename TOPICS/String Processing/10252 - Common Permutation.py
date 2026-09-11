import sys

lines = iter(sys.stdin)

for a_line in lines:
    a = a_line.rstrip("\n")
    b = next(lines).rstrip("\n")

    count_a = {}
    count_b = {}

    for char in a:
        count_a[char] = count_a.get(char, 0) + 1
    for char in b:
        count_b[char] = count_b.get(char, 0) + 1

    result = []
    for char in sorted(count_a):
        times = min(count_a[char], count_b.get(char, 0))
        result.append(char * times)

    print("".join(result))
