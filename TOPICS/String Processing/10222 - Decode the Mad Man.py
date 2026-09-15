import sys

row0 = "`1234567890-="
row1 = "qwertyuiop[]\\"
row2 = "asdfghjkl;'"
row3 = "zxcvbnm,./"

mapping = {}
for i in range(2, len(row0)):
    mapping[row0[i]] = row0[i - 2]
for i in range(2, len(row1)):
    mapping[row1[i]] = row1[i - 2]
for i in range(2, len(row2)):
    mapping[row2[i]] = row2[i - 2]
for i in range(2, len(row3)):
    mapping[row3[i]] = row3[i - 2]


for lines in sys.stdin:
    line = lines.rstrip("\n")

    result = []
    for char in line:
        if char == " ":
            result.append(" ")
        else:
            result.append(mapping[char])

    print("".join(result))
