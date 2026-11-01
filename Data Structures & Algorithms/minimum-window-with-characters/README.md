# Minimum Window Substring

**Topic:** Sliding Window  
**Difficulty:** Hard  
**Language:** Python

**Problem:** [Minimum Window Substring — NeetCode](https://neetcode.io/problems/minimum-window-with-characters)

## My Approach

In this problem, I need to find the smallest substring in `s` that contains all the characters of `t`, including their required frequencies.

For example:

- `s = "OUZODYXAZV"`
- `t = "XYZ"`
- **Output:** `"YXAZ"`

The tricky part is that I need to include every required character with the correct frequency, but I also need to make the window as small as possible.

I used the **sliding window approach** with two dictionaries to track character frequencies.

### How I Solved It

I created two dictionaries:

- `count_t` to store the frequency of each character required from `t`.
- `window` to store the frequency of characters inside my current window.

I also maintained:
- `have` to track how many required character frequencies are currently satisfied.
- `need` to store the number of distinct characters required.
- `res` to remember the starting and ending indices of the smallest valid window.
- `res_len` to track the minimum window length found so far.

Here's what I did:

1. First, I handled the cases where either string is empty or `s` is shorter than `t`.
2. I counted the frequency of every character in `t`.
3. I moved the `right` pointer through `s`, adding each character to the current window.
4. Whenever a character's frequency in the window became equal to its required frequency, I increased `have`.
5. When `have == need`, I knew the current window contained everything required.
6. While the window remained valid, I updated the smallest window if I found a shorter one.
7. Then I started shrinking the window from the left. If removing a character made its frequency fall below the required count, I decreased `have`.
8. I continued expanding and shrinking until I reached the end of `s`.

Finally, I returned the smallest valid substring. If no valid window was found, I returned an empty string.

### The Part I Need to Remember

The most important condition in my solution is:

`while have == need:`

This tells me that all the required character frequencies are satisfied.

Instead of stopping when I find the first valid window, I keep moving the left pointer forward to see whether I can make the window even smaller.

For example, if my current window contains all the characters I need, but also has some unnecessary characters at the beginning, I can remove those characters without making the window invalid.

I stop shrinking when removing a required character makes its frequency insufficient.

That's how I find the minimum window instead of just any valid window.

## Time and Space Complexity

Let:
- `n` = length of `s`
- `m` = length of `t`

- **Time:** `O(n + m)` average — I build the frequency map for `t` and move both pointers through `s`. Each pointer moves forward at most `n` times.
- **Space:** `O(n + m)` — the frequency dictionaries store characters from `t` and characters encountered in `s`. The space is bounded by the number of distinct characters encountered.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Sliding Window is useful for finding the smallest substring that satisfies certain conditions.
- Frequency dictionaries help me track how many times each character appears.
- The `have` and `need` variables make it easier to check whether the current window is valid.
- Expanding the window helps me include missing characters, while shrinking it helps me find a smaller valid answer.
- I need to check character frequencies, not just whether each required character exists.
- The minimum window problem requires both expanding and contracting the window.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace the `have` and `need` variables with a small example.
- [ ] Understand why `have` increases only when a frequency reaches the required count.
- [ ] Explain why I shrink the window only when `have == need`.
- [ ] Understand when and why `have` decreases.
- [ ] Test cases where no valid window exists and where `s` contains extra characters.
- [ ] Explain the time and space complexity in my own words.

---

*I'm learning that sliding window isn't just about moving two pointers. The important part is knowing exactly when a window becomes valid and how far I can shrink it without losing that validity.*
