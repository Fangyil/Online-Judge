# 不需考慮各種情況，直接以有沒有重疊來思考
total_nights = int(input())

night = 0
for _ in range(total_nights):
    night += 1
    guardian_a = list(map(int, input().split()))
    guardian_b = list(map(int, input().split()))

    overlap_width = max(
        0, min(guardian_a[2], guardian_b[2]) - max(guardian_a[0], guardian_b[0])
    )
    overlap_height = max(
        0, min(guardian_a[3], guardian_b[3]) - max(guardian_a[1], guardian_b[1])
    )
    strongly_secured = overlap_height * overlap_width

    weakly_secured = (
        (guardian_a[2] - guardian_a[0]) * (guardian_a[3] - guardian_a[1])
        + (guardian_b[2] - guardian_b[0]) * (guardian_b[3] - guardian_b[1])
        - 2 * strongly_secured
    )

    unsecured = 100 * 100 - strongly_secured - weakly_secured

    print(f"Night {night}: {strongly_secured} {weakly_secured} {unsecured}")
