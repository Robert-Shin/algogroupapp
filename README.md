# Option 1

Within option1.py there are two functions: findDuplicate and findDuplicateNaive.

The naive approach is the brute force O(n^2) method. For each element, we loop through the rest of the list and search for a matching element. There is no need to search the entire list since a past duplicate element would have been found in an earlier pass. This method does not use any extra space (O(1) space).

The faster approach involves taking advantage of the fact that every number between [1, N] appears exactly once. Using this knowledge, we add up the total sum we'd expect from the list and compare it with the actual sum of each element. We can then subtract the expected value from the observed value and deduce the extra number. This approach is O(n) time and also uses constant space O(1). 

Within test.py we randomly generate valid inputs and make sure that both functions work on all cases. I could not think of any other edge cases. 
Included is also a method of comparing the timing of the two methods. On 10 random cases with N = 10000, the linear solution takes ~ 0.02 seconds. The brute-force method takes 3.5 seconds on the same parameters.
