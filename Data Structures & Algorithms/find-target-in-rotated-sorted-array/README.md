# Search in Rotated Sorted Array

**Topic:** Binary Search  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Search in Rotated Sorted Array — NeetCode](https://neetcode.io/problems/find-target-in-rotated-sorted-array)

## My Approach

In this problem, I need to search for a target in a sorted array that has been rotated at an unknown pivot.

I used **Binary Search**, but there is one extra condition compared to normal Binary Search. At every iteration, I need to identify which half of the array is sorted.

Once I identify the sorted half, I check whether the target belongs to that range. Based on that, I eliminate the other half.

### How I Solved It

1. I initialized two pointers, `l` and `r`, at the beginning and end of the array.
2. I calculated the middle index.
3. If `nums[mid] == target`, I returned the middle index.
4. Otherwise, I checked whether the left half is sorted using `nums[l] <= nums[mid]`.
5. If the left half is sorted, I checked whether the target lies between `nums[l]` and `nums[mid]`.
   - If yes, I moved `r` to `mid - 1`.
   - Otherwise, I moved `l` to `mid + 1`.
6. If the left half is not sorted, the right half must be sorted.
   - I checked whether the target lies between `nums[mid]` and `nums[r]`.
   - If yes, I moved `l` to `mid + 1`.
   - Otherwise, I moved `r` to `mid - 1`.
7. If the target is not found, I returned `-1`.

### The Part I Need to Remember

The most important condition in this problem is:

`nums[l] <= nums[mid]`

This helps me identify whether the left half is sorted.

After that, I need to check whether the target belongs to that sorted range.

If it doesn't, I can safely eliminate that half and search the other side.

I also need to remember that the conditions use strict and non-strict comparisons carefully:

- `nums[l] <= target < nums[mid]`
- `nums[mid] < target <= nums[r]`

These boundaries help avoid missing the target.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(log n)` — I eliminate half of the search range in every iteration.
- **Space:** `O(1)` — I only use a few variables and don't create additional data structures.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Binary Search can be modified to work on rotated sorted arrays.
- At least one half of the array is always sorted when the elements are distinct.
- I can identify the sorted half by comparing `nums[l]` and `nums[mid]`.
- After identifying the sorted half, I check whether the target belongs to it.
- I should eliminate the half that cannot contain the target.
- This problem helped me understand how to apply Binary Search when the array is not completely sorted in its current arrangement.

## Practice Again

- [ ] Solve the problem again without looking at my code.
- [ ] Understand how to identify the sorted half.
- [ ] Remember the target-range conditions.
- [ ] Dry-run an example where the target is in the left sorted half.
- [ ] Dry-run an example where the target is in the right sorted half.
- [ ] Test a target that does not exist in the array.
- [ ] Explain why the time complexity is `O(log n)`.
- [ ] Implement the solution from scratch.

---

*I'm learning how to modify Binary Search for rotated arrays. The main thing I want to remember is to identify the sorted half first and then decide where the target can exist.*
