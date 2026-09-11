n = int(input())
text = {}

for _ in range(n):

    data = input().upper()
    for letter in data:
        if "A" <= letter <= "Z":
            text[letter] = text.get(letter, 0) + 1

sorted_text = sorted(
    text.items(),
    key=lambda item: (-item[1], item[0]),
)

for key, value in sorted_text:
    print(key, value)

