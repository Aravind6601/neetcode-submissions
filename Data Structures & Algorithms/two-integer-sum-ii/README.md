# Two Integer Sum II

**Topic:** Two Pointers  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Two Integer Sum II — NeetCode](https://neetcode.io/problems/two-integer-sum-ii)

## My Approach

In this problem, the array is already sorted, and I need to find two numbers whose sum equals the given target. Unlike the previous Two Sum problem, I don't need a dictionary here because the array is sorted.

I used the **two pointers approach**, starting one pointer at the beginning and the other at the end of the array.

### How I Solved It

1. I initialized `left` to `0` and `right` to the last index of the array.
2. I added the numbers at both pointers and stored their sum in `curr_sum`.
3. If the sum equals the target, I return their indices.
4. If the sum is greater than the target, I move `right` one position to the left to make the sum smaller.
5. If the sum is less than the target, I move `left` one position to the right to make the sum larger.
6. I keep repeating this until I find the pair.

One important thing I noticed is that the problem expects **1-based indices**, but Python lists use 0-based indexing. That's why I return `[left + 1, right + 1]`.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(n)` — in the worst case, the pointers move across the array only once.
- **Space:** `O(1)` — I only use a few variables and don't create any extra data structure.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Since the array is sorted, I can adjust the sum by moving the pointers instead of checking every possible pair.
- If the sum is too large, moving the right pointer left makes sense.
- If the sum is too small, moving the left pointer right helps increase it.
- Two pointers can reduce the time complexity from `O(n²)` with nested loops to `O(n)` without using extra space.
- I need to pay attention to whether a problem expects 0-based or 1-based indices.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Explain why moving the left or right pointer changes the sum in the required direction.
- [ ] Understand why this approach works because the array is sorted.
- [ ] Compare this solution with my previous Two Sum solution using a hash map.
- [ ] Explain the time and space complexity in my own words.

---

*I'm learning when a sorted array allows me to solve a problem with two pointers instead of an extra data structure.*
