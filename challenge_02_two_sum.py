def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}  # value → index

    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i

    raise ValueError("No two sum solution found")


# ===== Tests =====
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # (0, 1)
    print(two_sum([3, 2, 4], 6))        # (1, 2)
    print(two_sum([-1, 0, 1], 0))       # (0, 2)
    print(two_sum([3, 3], 6))           # (0, 1)
