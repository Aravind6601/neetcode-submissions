# Three Integer Sum (3Sum)

**Topic:** Two Pointers  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [3Sum — NeetCode](https://neetcode.io/problems/three-integer-sum)

## My Approach

In this problem, I need to find all unique triplets in an array whose sum is `0`.

For example, if the input is `[-1, 0, 1, 2, -1, -4]`, the answer is `[[-1, -1, 2], [-1, 0, 1]]`.

The main challenge is finding all valid triplets without returning duplicates. I used **sorting and two pointers** to solve it instead of checking every possible combination with three loops.

## How I Solved It

First, I sorted the array. This made it easier to find the required triplets because I could move pointers based on whether the sum was too small or too large.

1. I sorted `nums` in ascending order.
2. I fixed one number using the `i` pointer and used `left` and `right` to find the other two numbers.
3. If the current number was the same as the previous one, I skipped it to avoid generating duplicate triplets.
4. If `nums[i]` was greater than `0`, I stopped the loop because the remaining numbers would also be positive, so their sum couldn't be zero.
5. I calculated the sum of the three numbers:
   - If `total < 0`, I moved `left` forward to increase the sum.
   - If `total > 0`, I moved `right` backward to decrease the sum.
   - If `total == 0`, I added the triplet to `res` and moved both pointers.
6. After finding a valid triplet, I skipped repeated values at both pointers so I wouldn't add the same combination again.

### The Part I Need to Remember

Skipping duplicates is important in this problem. Even if I find the correct triplets, I can still return repeated combinations if I don't handle duplicate values properly.

Sorting makes this easier because equal numbers appear next to each other.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(n²)` — sorting takes `O(n log n)`, and for each fixed number, the two pointers scan the remaining array in linear time.
- **Space:** `O(n)` auxiliary space in Python's sorting implementation, excluding the output. The two-pointer search itself uses `O(1)` extra space.

The result list requires additional space depending on how many unique triplets are found.

## My Solution

[View submission-1.py](./submission-1.py)

## What I Learned

- Sorting can make searching for combinations much easier.
- Two pointers help me find the other two numbers without using three nested loops.
- Skipping duplicate values is necessary when the output must contain unique triplets.
- Once the fixed number becomes positive, I can stop searching because the array is sorted.
- This problem combines sorting, two pointers, and careful handling of edge cases.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Explain why sorting is necessary for my pointer movements.
- [ ] Understand why I skip duplicates at `i`, `left`, and `right`.
- [ ] Explain why the loop can stop when `nums[i] > 0`.
- [ ] Walk through an example where the array contains several duplicate numbers.
- [ ] Explain why the time complexity is `O(n²)`.

---

*The important thing is not just finding the triplets, but understanding how sorting and two pointers reduce the work while avoiding duplicates.*
