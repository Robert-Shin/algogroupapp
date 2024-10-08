from option1 import findDuplicate, findDuplicateNaive
from random import randint, shuffle
from time import perf_counter

def test_edge_cases() -> None:
    input = [1,1]
    assert findDuplicate(input) == 1
    assert findDuplicateNaive(input) == 1

def test_random_data(size: int) -> None:
    input = [i+1 for i in range(size)]
    extra = randint(1, size)
    input.append(extra)
    shuffle(input)
    assert findDuplicate(input) == extra
    #assert findDuplicateNaive(input) == extra

if __name__ == "__main__":
    test_edge_cases()
    start = perf_counter()
    for i in range(10):
        test_random_data(10000)
    print("All cases passed")
    print(f"Time elapsed: {perf_counter() - start}")