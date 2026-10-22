# Longest Consecutive Sequence

**Topic:** Arrays & Hashing  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Longest Consecutive Sequence — NeetCode](https://neetcode.io/problems/longest-consecutive-sequence)

## My Approach

In this problem, I need to find the length of the longest sequence of consecutive numbers in an unsorted array.

For example, if the input is `[100, 4, 200, 1, 3, 2]`, the answer is `4` because the longest consecutive sequence is `[1, 2, 3, 4]`.

My approach was to use a **set** so I could check whether a number exists in the array without searching through the entire list every time.

### How I Solved It

1. First, I converted the input list into a set called `n`. This also removes duplicate numbers.
2. I went through each number in the set.
3. Before starting a sequence, I checked whether the previous number (`i - 1`) exists in the set.
4. If it doesn't exist, that means I've found the beginning of a sequence. I started counting consecutive numbers from there.
5. I kept checking whether the next number existed in the set and increased the length until the sequence ended.
6. Finally, I updated `longest` whenever I found a longer sequence and returned it.

### Why I Check for `i - 1`

This is the important part of my solution.

I don't want to start counting from every number because that would repeat a lot of work. By checking whether `i - 1` exists, I only start counting when the current number is the beginning of a sequence.

For example, with `[1, 2, 3, 4]`, I start counting from `1`, not from `2`, `3`, or `4`.

This is what helps me achieve linear time complexity on average.

## Time and Space Complexity

Let `n` be the number of elements in the input array.

- **Time:** `O(n)` average — creating the set and checking the sequences take linear time overall.
- **Space:** `O(n)` — the set can store all the unique numbers.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A set is useful when I need fast membership checks.
- Sorting isn't always necessary to solve problems involving consecutive numbers.
- Checking for the beginning of a sequence helps avoid repeating unnecessary work.
- Sometimes the key to optimizing a solution is figuring out when **not** to start processing something.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why I check `i - 1` before counting a sequence.
- [ ] Test the solution with an empty array, duplicate numbers, and negative numbers.
- [ ] Explain why the algorithm takes O(n) time on average.
- [ ] Compare this approach with sorting the array first.

---

*I'm learning that choosing the right data structure can make a big difference. The goal is to understand why the optimization works, not just remember the code.*
