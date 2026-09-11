test_case = int(input())


for _ in range(test_case):
    num = int(input())

    binary_bit = bin(num).count("1")
    hexadecimal_bit = bin(int(str(num), 16)).count("1")

    print(binary_bit, hexadecimal_bit)
