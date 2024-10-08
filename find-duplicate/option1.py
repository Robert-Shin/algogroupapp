# OPTION 1 - FIND DUPLICATE
# DO NOT SHARE

from typing import List

# Implement a function to identify a duplicate integer in an unsorted array
# of integers. Talk about time/space complexity for each method you implement.

# `input` contains exactly N+1 numbers
# `input` elements are integers in the domain [1, N]
# `input` contains all integers in the domain [1, N] at least once
# `findDuplicate` returns an `int`: the duplicate integer
def findDuplicate(input: List[int]) -> int:
    target = 0
    count = 0
    for i in range(len(input)):
        target += i
        count += input[i]
    return count - target


def findDuplicateNaive(input: List[int]) -> int:
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            if input[i] == input[j]:
                return input[i]
