# Median of Two Sorted Arrays

**Topic:** Binary Search  
**Difficulty:** Hard  
**Language:** Python

**Problem:** [Median of Two Sorted Arrays](https://neetcode.io/problems/median-of-two-sorted-arrays)

## My Approach

The main idea is to use binary search to divide both arrays into two parts such that:

- Every element in the left partition is less than or equal to every element in the right partition.
- The left partition contains half of the total elements (or one extra element when the total is odd).

Instead of merging both arrays, I perform binary search on the smaller array and calculate the corresponding partition in the other array.

### How I Solved It

1. First, I make sure `A` is the smaller array. This keeps the binary search efficient.
2. Calculate the total number of elements and how many should be in the left partition.
3. Use binary search to choose a partition index `i` in `A`.
4. Calculate the partition index `j` in `B` using `half - i`.
5. Check the four boundary values:
   - `A_left` and `A_right`
   - `B_left` and `B_right`
6. If the partition is correct:
   - For an odd number of elements, return the maximum of the two left values.
   - For an even number of elements, take the average of the maximum left value and minimum right value.
7. If the partition is incorrect, adjust the binary search range.

I used negative and positive infinity for missing boundary values. This avoids writing separate conditions for partitions at the beginning or end of an array.

### The Part I Need to Remember

The important condition for a correct partition is:

```python
A_left <= B_right and B_left <= A_right
```

- If `A_left > B_right`, move the partition in `A` to the left.
- Otherwise, move it to the right.

**Key pattern:** Binary Search on Partition.

## Time and Space Complexity

- **Time Complexity:** `O(log(min(m, n)))` — Binary search is performed only on the smaller array.
- **Space Complexity:** `O(1)` — Only a fixed number of variables are used. No additional array is created.

Here, `m` and `n` are the lengths of the two input arrays.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Binary search can be used to find a correct partition, not just a target element.
- We don't always need to merge sorted arrays to calculate their median.
- Searching the smaller array helps achieve the optimal time complexity.
- Using infinity as a boundary value makes edge cases easier to handle.

## Practice Again

- [ ] Explain why we always binary search on the smaller array.
- [ ] Understand how `i` and `j` determine the partition sizes.
- [ ] Dry-run the partition condition with odd and even total lengths.
- [ ] Understand why infinity is used for missing boundaries.
- [ ] Implement the solution again without looking at the code.

This problem helped me understand a more advanced use of binary search. The key is not searching for an element, but finding the correct partition.
