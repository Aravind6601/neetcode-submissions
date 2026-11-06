# Find Minimum in Rotated Sorted Array

**Topic:** Binary Search  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Find Minimum in Rotated Sorted Array — NeetCode](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)

## My Approach

In this problem, I need to find the minimum element in a sorted array that has been rotated at some unknown pivot.

For example, an array like `[1, 2, 3, 4, 5]` can become `[3, 4, 5, 1, 2]` after rotation.

Instead of checking every element one by one, I used **Binary Search** to find the minimum efficiently.

The key idea is to compare the middle element with the rightmost element to identify which part of the array contains the minimum.

### How I Solved It

I used two pointers, `l` and `r`, to keep track of the current search range.

1. I initialized `l = 0` and `r = len(nums) - 1`.
2. As long as `l < r`, I calculated the middle index using `(l + r) // 2`.
3. If `nums[mid] > nums[r]`, it means the minimum must be somewhere on the right side of `mid`. So I moved `l` to `mid + 1`.
4. Otherwise, the minimum could be the middle element itself or somewhere on its left side. So I moved `r` to `mid`.
5. I repeated this process until both pointers pointed to the same index.
6. Finally, I returned `nums[l]`, which is the minimum element.

### The Part I Need to Remember

The most important part of my solution is this comparison:

`nums[mid] > nums[r]`

I need to understand why comparing the middle element with the rightmost element helps me decide which half to eliminate.

For example, consider:

`nums = [3, 4, 5, 1, 2]`

- If `nums[mid] > nums[r]`, the minimum is on the right side because the rotation point must be there.
- If `nums[mid] <= nums[r]`, the right portion is sorted, so the minimum is either `mid` itself or somewhere on the left.

One important thing I need to remember is why I use:

`r = mid`

instead of `r = mid - 1`.

This is because `mid` itself could be the minimum element. If I remove it from the search range, I might lose the answer.

Also, the loop condition is `l < r` because I only need to continue searching until both pointers meet.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(log n)` — Binary Search reduces the search range by half in every iteration.
- **Space:** `O(1)` — I only use a few variables and don't create any additional data structures.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Binary Search can also be used on rotated sorted arrays.
- Comparing the middle element with the rightmost element helps identify which side contains the minimum.
- I should use `r = mid` because the middle element itself could be the answer.
- The loop condition `l < r` helps narrow the search until both pointers meet.
- I don't need to actually find the rotation point separately. Binary Search can directly locate the minimum element.
- This problem helped me understand how to modify normal Binary Search when the array is not completely sorted in its current arrangement.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why I compare `nums[mid]` with `nums[r]`.
- [ ] Trace `l`, `r`, and `mid` using `[3, 4, 5, 1, 2]`.
- [ ] Test an array that is not rotated, such as `[1, 2, 3, 4, 5]`.
- [ ] Understand why I use `r = mid` instead of `r = mid - 1`.
- [ ] Explain why the loop condition is `l < r`.
- [ ] Explain why the time complexity is `O(log n)`.
- [ ] Try implementing the solution again from scratch.

---

*I'm learning how Binary Search can work even when an array has been rotated. The main thing I want to remember is how comparing the middle and rightmost elements helps me decide which half to eliminate.*
