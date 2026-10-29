# Longest Substring Without Repeating Characters

**Topic:** Sliding Window  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Longest Substring Without Repeating Characters — NeetCode](https://neetcode.io/problems/longest-substring-without-duplicates)

## My Approach

In this problem, I need to find the length of the longest substring that doesn't contain any repeated characters.

For example, if the input is `"abcabcbb"`, the answer is `3` because `"abc"` is the longest substring without repeating characters.

I used the **sliding window approach** with a dictionary to keep track of the last position where each character appeared.

### How I Solved It

I used two pointers, `left` and `right`, to represent the current window. I also created a dictionary called `char_index` to store each character's most recent index.

1. I moved `right` through the string one character at a time using `enumerate()`.
2. For every character, I checked whether it was already in the dictionary and whether its previous occurrence was still inside the current window.
3. If it was repeated inside the window, I moved `left` to the position immediately after its previous occurrence.
4. I updated the character's index in the dictionary.
5. I calculated the current window length using `right - left + 1` and updated `max_len` whenever I found a longer substring.
6. After checking the entire string, I returned `max_len`.

### The Part I Need to Remember

The important condition in my code is:

`char_index[char] >= left`

Just because a character appeared earlier doesn't mean it's necessarily repeated inside my current window. Its previous position might already be outside the window.

For example, in `"abba"`, when I reach the last `"a"`, I shouldn't move `left` backwards. The previous `"a"` is already outside the current window.

That's why I check whether the previous index is greater than or equal to `left` before moving the window.

## Time and Space Complexity

Let `n` be the length of the string.

- **Time:** `O(n)` — I traverse the string once, and dictionary lookups and updates take O(1) time on average.
- **Space:** `O(n)` — in the worst case, the dictionary can store the index of every character if all characters are distinct.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Sliding windows help me solve substring problems without checking every possible substring.
- A dictionary can store the last seen index of each character.
- The `left` pointer should only move forward, never backward.
- I need to check whether a repeated character is inside the current window, not just whether I've seen it before.
- Updating the maximum window length at every step helps me keep track of the best answer.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace both pointers using `"abcabcbb"` and `"abba"`.
- [ ] Explain why I check `char_index[char] >= left`.
- [ ] Understand why I use `right - left + 1` to calculate the window length.
- [ ] Explain why the solution takes O(n) time.
- [ ] Try solving it using a set instead of a dictionary.

---

*I'm learning how to maintain a sliding window efficiently. The key is knowing when to move the window and when a previously seen character actually matters.*
