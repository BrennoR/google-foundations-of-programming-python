# maxSpan
from collections import defaultdict


# Time - O(N), Space - O(N)
def maxSpan(arr: [int]) -> int:
    if len(arr) == 0:
        return 0

    indices = defaultdict(int)
    for idx, val in enumerate(arr):
        indices[val] = idx

    max_span = 1
    for idx, val in enumerate(arr):
        span = indices[val] - idx + 1
        if span > max_span:
            max_span = span

    return max_span


print(maxSpan([1, 2, 1, 1, 3]))
print(maxSpan([1, 4, 2, 1, 4, 1, 4]))
print(maxSpan([1, 4, 2, 1, 4, 4, 4]))
