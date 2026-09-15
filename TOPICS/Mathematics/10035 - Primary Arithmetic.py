import sys

for lines in sys.stdin:
    a, b = map(int, lines.split())

    if a == 0 and b == 0:
        break

    carry_total = 0
    carry_next = 0
    while a != 0 or b != 0:
        carry_now = carry_next
        carry_next = 0

        a_mod = a % 10
        b_mod = b % 10
        a //= 10
        b //= 10

        if a_mod + b_mod + carry_now > 9:
            carry_total += 1
            carry_next = 1

    if carry_total == 0:
        print("No carry operation.")
    elif carry_total == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_total} carry operations.")
