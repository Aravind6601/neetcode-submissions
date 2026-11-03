# Binary Search

**Topic:** Binary Search  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Binary Search — NeetCode](https://neetcode.io/problems/binary-search)

## My Approach

In this problem, I need to find a target number in a sorted array and return its index. If the target doesn't exist, I should return `-1`.

Since the array is already sorted, I don't need to check every element one by one. I used **Binary Search** to reduce the search area by half at every step.

### How I Solved It

I used two pointers, `left` and `right`, to keep track of the portion of the array I'm currently searching.

1. I started `left` at the first index and `right` at the last index.
2. As long as `left <= right`, I calculated the middle index using `left + (right - left) // 2`.
3. If the middle element matched the target, I returned its index.
4. If the middle element was smaller than the target, I moved `left` to `mid + 1` because the target could only be on the right side.
5. If the middle element was greater than the target, I moved `right` to `mid - 1` because the target could only be on the left side.
6. If the search range became empty without finding the target, I returned `-1`.

### The Part I Need to Remember

The main idea is that I don't have to search the entire array after every comparison.

For example, if the middle element is smaller than my target, I can completely ignore the left half because the array is sorted.

Similarly, when the middle element is greater than the target, I can ignore the right half.

One more thing I need to remember is why I use:

`left <= right`

This ensures that even when only one element remains in the search range, I still check it.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(log n)` — every comparison reduces the remaining search range approximately by half.
- **Space:** `O(1)` — I only use a few variables and don't create any additional data structures.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Binary Search works efficiently when the array is sorted.
- I can eliminate half of the search space after every comparison.
- Updating `left` to `mid + 1` and `right` to `mid - 1` avoids checking the same elements again.
- The loop condition `left <= right` ensures that the last remaining element is also checked.
- Binary Search reduces the search time from `O(n)` to `O(log n)`.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace `left`, `right`, and `mid` using a small example.
- [ ] Test cases where the target is at the beginning, middle, and end.
- [ ] Test a case where the target doesn't exist.
- [ ] Explain why the array must be sorted.
- [ ] Explain why the time complexity is `O(log n)`.
- [ ] Try implementing Binary Search from scratch.

---

*I'm learning how sorted data can help eliminate unnecessary work. The main thing I want to remember is how each comparison reduces the search space by half.*
