# Valid Anagram

**Topic:** Arrays & Hashing  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Valid Anagram — NeetCode](https://neetcode.io/problems/is-anagram)

## My Approach

In this problem, I need to check whether two strings are anagrams of each other.

Two strings are anagrams when they contain exactly the same characters with the same frequencies, even if the characters appear in a different order.

For example, `"racecar"` and `"carrace"` are anagrams, but `"hello"` and `"world"` are not.

### How I Solved It

I used two dictionaries to count the characters in both strings.

1. First, I checked whether both strings have the same length. If not, I returned `False`.
2. I created two empty dictionaries, `count_s` and `count_t`.
3. I went through each string and counted how many times each character appeared.
4. Finally, I compared the character counts. If any count was different, I returned `False`. Otherwise, I returned `True`.

I used the `.get()` method to retrieve a character's count safely, even when that character doesn't exist in the second dictionary.

## Time and Space Complexity

Let `n` be the length of each string and `u` be the number of distinct characters.

- **Time:** `O(n)` — I traverse both strings and compare their character counts.
- **Space:** `O(u)` — I store the character frequencies in two dictionaries.

In the general case, the space complexity is `O(n)`.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Anagrams must have the same character frequencies, not necessarily the same character order.
- Dictionaries make it easy to count how many times each character appears.
- Checking the lengths first helps eliminate impossible cases early.
- The `.get()` method is useful when working with dictionary values that might not exist.

## Practice Again

- [ ] Solve the problem again without looking at my code.
- [ ] Try solving it using `Counter` from Python's `collections` module.
- [ ] Try solving it by sorting both strings and comparing them.
- [ ] Explain the time and space complexity in my own words.

---

*DSA practice — understanding the logic instead of just memorizing the solution.*
