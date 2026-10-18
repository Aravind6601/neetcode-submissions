# Two Sum

**Topic:** Arrays & Hashing  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Two Sum — NeetCode](https://neetcode.io/problems/two-integer-sum)

## My Approach

In this problem, I need to find the indices of two numbers whose sum is equal to the given target.

For example, if `nums = [2, 7, 11, 15]` and `target = 9`, the answer is `[0, 1]` because `2 + 7 = 9`.

My idea was to check whether the number needed to complete the target was already seen while going through the array.

### How I Solved It

I used a dictionary called `prev` to store numbers along with their indices.

1. I went through the array using `enumerate()` so I could access both the number and its index.
2. For every number, I calculated the difference using `target - n`.
3. I checked whether that difference was already present in the dictionary.
4. If it was present, I returned the index of that number and the current index.
5. Otherwise, I stored the current number and its index in the dictionary.

The important thing is that I check for the required number before storing the current number. This helps avoid using the same element twice.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(n)` on average — I traverse the array once, and dictionary lookups take constant time on average.
- **Space:** `O(n)` — in the worst case, I may store almost every number in the dictionary.

## My Solution

[View submission-2.py](./submission-2.py)

## What I Learned

- A dictionary can store both values and their indices.
- Instead of checking every possible pair, I can search for the required complement.
- Checking the complement before storing the current number avoids using the same element twice.
- Using a hash map improves the average time complexity from `O(n²)` with nested loops to `O(n)`.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Explain why I calculate `target - n`.
- [ ] Understand why I check the dictionary before adding the current number.
- [ ] Try solving it using nested loops and compare both approaches.
- [ ] Explain the time and space complexity in an interview.

---

*One problem at a time. My goal is to understand the logic well enough to solve it on my own next time.*
