# Group Anagrams

**Topic:** Arrays & Hashing  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Group Anagrams on NeetCode](https://neetcode.io/problems/anagram-groups)

## My Approach

At first, I was thinking about how to identify which words are anagrams of each other. Then I realized that if I sort the characters in each word, all its anagrams will look the same.

For example:

- `"act"` → `"act"`
- `"cat"` → `"act"`
- `"tac"` → `"act"`

So I used a dictionary to group words that have the same sorted form.

Here's what I did:
1. Created a dictionary using `defaultdict(list)`.
2. Took each word and sorted its characters.
3. Used the sorted word as the dictionary key.
4. Added the original word to that key's list.
5. Returned all the grouped words.

## Time and Space Complexity

Let `n` be the number of words and `k` be the maximum length of a word.

- **Time:** `O(n * k log k)` — because I sort every word.
- **Space:** `O(n * k)` — to store the words in groups and their dictionary keys.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Sorting can help identify anagrams without comparing every word with every other word.
- A dictionary helps group items that share the same key.
- `defaultdict(list)` makes it easier to add items without checking whether a key already exists.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Try solving it using character frequencies instead of sorting.
- [ ] Explain the approach and complexity without referring to these notes.
