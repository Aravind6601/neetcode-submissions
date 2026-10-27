# Trapping Rain Water

**Topic:** Two Pointers  
**Difficulty:** Hard  
**Language:** Python

**Problem:** [Trapping Rain Water — NeetCode](https://neetcode.io/problems/trapping-rain-water)

## My Approach

In this problem, I need to calculate how much rainwater can be trapped between the bars after it rains.

The amount of water trapped at a position depends on the tallest bar on its left and the tallest bar on its right. The water level is limited by whichever of these two heights is smaller.

I used the **two pointers approach** to solve this without creating separate arrays to store the maximum heights from both sides.

### How I Solved It

I started with two pointers, `left` at the beginning and `right` at the end of the array.

I also maintained two variables:
- `left_max` to track the tallest bar seen from the left.
- `right_max` to track the tallest bar seen from the right.

Then I followed these steps:

1. If the height array is empty, I return `0`.
2. I compare `left_max` and `right_max`.
3. If `left_max` is smaller, I move the `left` pointer one step forward and update `left_max`.
4. I calculate the water trapped at that position using `left_max - height[left]` and add it to `trap_water`.
5. Otherwise, I move the `right` pointer one step backward, update `right_max`, and add `right_max - height[right]` to the total.
6. I repeat this until the pointers meet, then return the total trapped water.

### The Part I Need to Understand

The important part is why I compare `left_max` and `right_max` before moving a pointer.

When `left_max` is smaller than `right_max`, I know the right side has a taller boundary than the maximum height I've seen from the left. So I can calculate the water at the next left position using `left_max`.

The same logic works in reverse when `right_max` is smaller or equal: I can process the next position from the right using `right_max`.

This lets me calculate the trapped water one position at a time without needing to know the exact maximum height on both sides for every position.

## Time and Space Complexity

Let `n` be the number of bars.

- **Time:** `O(n)` — the two pointers move through the array, and each position is processed in constant time.
- **Space:** `O(1)` — I only use a few variables to track the pointers, maximum heights, and total water.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- The water trapped at a position depends on the maximum heights on both sides.
- Two pointers can help calculate the answer without storing separate prefix and suffix maximum arrays.
- Tracking `left_max` and `right_max` allows me to process a position when its contribution can be determined.
- Moving the pointer on the side with the smaller maximum height is the key idea behind this solution.
- Understanding why a pointer moves is more useful than simply memorizing the code.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace `left`, `right`, `left_max`, and `right_max` with a small example.
- [ ] Understand why comparing the maximum heights helps determine which side to process.
- [ ] Test an empty array, an increasing array, and a decreasing array.
- [ ] Explain why the solution uses `O(1)` extra space.
- [ ] Compare this approach with using prefix and suffix maximum arrays.

---

*I'm learning how to use information from both ends of an array to solve a problem efficiently without storing extra arrays.*
