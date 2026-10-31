# Permutation in String

**Topic:** Sliding Window  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Permutation in String — NeetCode](https://neetcode.io/problems/permutation-string)

## My Approach

In this problem, I need to check whether `s2` contains any permutation of `s1` as a substring.

A permutation means the characters can be arranged in any order, but their frequencies must remain the same.

For example:

- `s1 = "ab"`
- `s2 = "eidbaooo"`
- **Output:** `True`

This is because `"ba"` is present in `s2`, and it contains the same characters as `s1`.

I used the **fixed-size sliding window approach** with two frequency arrays to solve this problem.

### How I Solved It

I created two arrays of size 26 because the problem contains lowercase English letters.

- `s1_count` stores the frequency of characters in `s1`.
- `s2_count` stores the frequency of characters in the current window of `s2`.

Here's what I did:

1. First, I checked whether `s1` is longer than `s2`. If it is, I immediately return `False`.
2. I counted the frequency of every character in `s1` and the first window of `s2`.
3. I created a variable called `matches` to count how many of the 26 character frequencies are equal between both arrays.
4. I then started sliding the window through `s2`.
5. Whenever I moved the window, I added the new character entering from the right and removed the character leaving from the left.
6. After each update, I adjusted `matches` based on whether that character's frequency became equal or unequal between the two arrays.
7. If `matches == 26`, all character frequencies match, so I returned `True`.

If no window matches after checking the entire string, I return `False`.

### The Part I Need to Remember

The interesting part of my solution is the `matches` variable.

Instead of comparing both frequency arrays completely every time the window moves, I track how many character frequencies currently match.

For example, suppose the frequency of `a` in both arrays is 2. That contributes one match.

When a character enters or leaves the window, I only update the match count for that particular character.

So:

- If its frequency becomes equal in both arrays, I increase `matches`.
- If its frequency becomes unequal, I decrease `matches`.

When all 26 characters match, I know that the current window is a permutation of `s1`.

This avoids comparing all 26 characters again after every window movement.

## Time and Space Complexity

Let:
- `n` = length of `s1`
- `m` = length of `s2`

- **Time:** `O(n + m + 26)`, which simplifies to `O(n + m)`. I first count the characters, compare the 26 frequencies, and then slide through `s2`.
- **Space:** `O(1)` — I only use two fixed-size arrays of 26 elements and a few variables.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A permutation can be identified by comparing character frequencies instead of generating every possible arrangement.
- Fixed-size sliding windows are useful when the substring length is already known.
- Two frequency arrays help compare the characters in the original string and current window.
- The `matches` variable avoids repeatedly comparing all 26 character frequencies.
- When a character enters or leaves the window, only its frequency needs to be checked and updated.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why the window size must always equal `len(s1)`.
- [ ] Trace the `matches` variable using `s1 = "ab"` and `s2 = "eidbaooo"`.
- [ ] Explain why `matches == 26` means the window is a valid permutation.
- [ ] Understand why I update `matches` when adding and removing characters.
- [ ] Explain the time and space complexity in my own words.
- [ ] Try solving it without using the `matches` optimization.

---

*I'm learning how to combine sliding windows with frequency counting. The interesting part is finding ways to update only what changes instead of comparing everything again.*
