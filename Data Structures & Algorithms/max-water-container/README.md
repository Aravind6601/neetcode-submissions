# Container With Most Water

**Topic:** Two Pointers  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Container With Most Water — NeetCode](https://neetcode.io/problems/max-water-container)

## My Approach

In this problem, I need to find two lines that can hold the maximum amount of water between them.

The amount of water depends on two things: the distance between the lines and the height of the shorter line. Even if one line is very tall, the shorter line limits how much water the container can hold.

I used the **two pointers approach** to solve this without checking every possible pair.

### How I Solved It

I started with two pointers, `l` at the beginning of the array and `r` at the end.

1. I calculated the width using `r - l`.
2. I found the height of the container using `min(heights[l], heights[r])`.
3. I multiplied the width by the shorter height to calculate the current area.
4. I updated `max_water` whenever I found a larger area.
5. If the left line was shorter, I moved `l` one step forward. Otherwise, I moved `r` one step backward.
6. I repeated this until both pointers met and returned the maximum area.

### Why I Move the Shorter Line

This is the main idea I need to remember from this problem.

The shorter line limits the water level. Moving the taller line inward would reduce the width without giving me a better possible height from that side.

By moving the shorter line, I get a chance to find a taller line that might produce a larger area, even though the width decreases.

This helps me avoid checking every pair with nested loops.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(n)` — the pointers move toward each other, and each step eliminates one position.
- **Space:** `O(1)` — I only use a few variables and don't create any additional data structures.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- The area is calculated using `width * min(left_height, right_height)`.
- The shorter line determines the maximum possible water height for a pair.
- Two pointers help reduce the time complexity from `O(n²)` with nested loops to `O(n)`.
- Moving the shorter line is what makes the optimization work.
- I should understand why a pointer moves instead of memorizing the implementation.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace the pointer movements with a small example.
- [ ] Explain why the shorter line determines the water level.
- [ ] Understand why moving the shorter line makes sense.
- [ ] Explain the time and space complexity in my own words.

---

*I'm learning to recognise when two pointers can eliminate unnecessary comparisons and make a solution more efficient.*
