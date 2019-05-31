# canBalance


def canBalance(arr: [int]) -> bool:
    if not arr:
        return True

    left_sum = sum(arr)
    right_sum = 0
    idx = len(arr) - 1
    while left_sum > right_sum:
        left_sum -= arr[idx]
        right_sum += arr[idx]
        idx -= 1

    return left_sum == right_sum


print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))
