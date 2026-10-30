# Longest Repeating Character Replacement

**Topic:** Sliding Window  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Longest Repeating Character Replacement — NeetCode](https://neetcode.io/problems/longest-repeating-substring-with-replacement)

## My Approach

In this problem, I need to find the length of the longest substring where I can make all characters the same by replacing at most `k` characters.

For example, if `s = "AABABBA"` and `k = 1`, the answer is `4`. I can replace one character in `"AABA"` to make all four characters the same.

I used the **sliding window approach** with a dictionary to keep track of character frequencies inside the window.

### How I Solved It

I maintained two pointers, `left` and `right`, to represent my current window. I also used:

- `count` to store the frequency of each character.
- `max_freq` to track the highest character frequency seen while expanding the window.
- `max_len` to store the longest window length found.

Here's what I did:

1. I moved `right` through the string one character at a time.
2. For every character, I increased its frequency in the dictionary.
3. I updated `max_freq` whenever I found a higher character frequency.
4. I calculated how many characters would need to be replaced using:

   `window_length - max_freq`

5. If this number was greater than `k`, it meant I needed more replacements than allowed. So I reduced the frequency of the leftmost character and moved `left` forward.
6. After adjusting the window, I calculated its length and updated `max_len` if I found a longer one.
7. Finally, I returned `max_len`.

### The Part I Need to Remember

The main condition in this problem is:

`(right - left + 1) - max_freq > k`

Why?

The most frequent character already occupies `max_freq` positions in the current window. I only need to replace the remaining characters to make the entire window contain the same character.

For example, if my window is `"AABAB"`, the most frequent character is `A`, which appears 3 times.

- Window length = 5
- Maximum frequency = 3
- Replacements needed = 5 - 3 = 2

If `k = 2`, this window is possible.

One important detail in my implementation is that I don't decrease `max_freq` when the left pointer moves. It keeps the highest frequency seen while expanding the window, even if that character's current window frequency later becomes smaller.

This is an intentional optimization. It avoids repeatedly recalculating the maximum frequency. Although the current window isn't always strictly valid after shrinking, this approach still gives the correct maximum length.

## Time and Space Complexity

Let `n` be the length of the string.

- **Time:** `O(n)` — the right pointer traverses the string once, and the left pointer only moves forward.
- **Space:** `O(1)` — the dictionary stores frequencies of uppercase English letters, so its size is bounded by 26.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Sliding Window is useful for finding the longest substring that satisfies a condition.
- A frequency dictionary helps me track repeated characters inside a window.
- The difference between window length and maximum character frequency tells me how many replacements are required.
- I don't always need to recalculate the maximum frequency after shrinking the window.
- Understanding why `max_freq` is not decreased is important for explaining this optimized solution.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Trace the window using `"AABABBA"` with `k = 1`.
- [ ] Explain why `window_length - max_freq` gives the replacements needed.
- [ ] Understand why `max_freq` is not decreased when the left pointer moves.
- [ ] Explain how both pointers help achieve O(n) time.
- [ ] Try implementing the solution again from scratch.

---

*I'm learning to maintain a sliding window using frequency counts and understand when an optimization can save unnecessary calculations.*
