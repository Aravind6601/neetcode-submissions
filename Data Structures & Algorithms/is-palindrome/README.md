# Valid Palindrome

**Topic:** Two Pointers  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Valid Palindrome — NeetCode](https://neetcode.io/problems/is-palindrome)

## My Approach

In this problem, I need to check whether a string is a palindrome. The tricky part is that I have to ignore spaces, punctuation, and special characters, and treat uppercase and lowercase letters as the same.

For example, `"A man, a plan, a canal: Panama"` is a palindrome because, after ignoring the non-alphanumeric characters and case differences, the string reads the same forward and backward.

I used the **two pointers approach** instead of creating a separate cleaned string.

### How I Solved It

I started with two pointers: `left` at the beginning of the string and `right` at the end.

1. I moved the `left` pointer forward whenever it encountered a character that wasn't alphanumeric.
2. Similarly, I moved the `right` pointer backward until it reached an alphanumeric character.
3. I compared both characters after converting them to lowercase.
4. If they didn't match, I immediately returned `False`.
5. If they matched, I moved both pointers toward the centre and continued checking.
6. If the pointers crossed or met without finding a mismatch, I returned `True`.

### Why I Used Two Pointers

Instead of creating another string after removing spaces and punctuation, I can compare characters directly from both ends.

This also means I don't need to store a cleaned version of the original string. I just keep moving the pointers until the entire string has been checked.

## Time and Space Complexity

Let `n` be the length of the string.

- **Time:** `O(n)` — the two pointers move through the string, and each character is checked at most a constant number of times.
- **Space:** `O(1)` auxiliary space — I only use two pointers and don't create another string.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Two pointers can help compare a string from both ends.
- `isalnum()` helps me skip characters that aren't letters or numbers.
- `lower()` allows me to compare characters without worrying about uppercase and lowercase differences.
- I can solve this problem without modifying the original string or creating a cleaned copy.
- Returning early when I find a mismatch avoids unnecessary comparisons.

## Practice Again

- [ ] Solve the problem again without looking at my code.
- [ ] Understand why I skip non-alphanumeric characters on both sides.
- [ ] Test an empty string, a single character, and a string containing only punctuation.
- [ ] Explain why the solution works with two pointers.
- [ ] Explain the time and space complexity in my own words.

---

*Another problem completed. I'm learning to recognise when two pointers can simplify a solution and save extra space.*
