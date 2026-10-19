# Encode and Decode Strings

**Topic:** Arrays & Hashing  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Encode and Decode Strings — NeetCode](https://neetcode.io/problems/string-encode-and-decode)

## My Approach

In this problem, I need to convert a list of strings into a single string and then convert it back to the original list.

The tricky part is that the strings can contain different characters, so simply joining them with a separator might not work in every case. I need a way to know exactly where each string starts and ends.

### How I Solved It

I used the length of each string followed by a `#` separator to encode it.

For example, the list `["hello", "world"]` becomes:

`5#hello5#world`

Here, `5#` tells me that the next 5 characters belong to the first string. After that, I can read the next length and continue.

### Encoding

1. I started with an empty string called `result`.
2. For every string, I added its length, followed by `#`, followed by the actual string.
3. After processing all the strings, I returned the combined string.

### Decoding

1. I used two pointers, `i` and `j`, to find the length information.
2. Starting from `i`, I moved `j` until I found the `#` separator.
3. I converted the characters before `#` into an integer to get the length of the next string.
4. Using that length, I extracted the exact string and added it to the result list.
5. Then I moved `i` to the beginning of the next encoded string and repeated the process.

The main idea is that I don't need to search for the end of each actual string. I already know its length, so I can extract it directly.

## Time and Space Complexity

Let `L` be the total number of characters across all input strings, excluding the encoding information.

- **Time:** `O(L + n)` for both encoding and decoding, assuming string construction is linear overall. Here, `n` is the number of strings.
- **Space:** `O(L + n)` for the encoded string or the decoded list and its contents.

## My Solution

[View submission-1.py](./submission-1.py)

## What I Learned

- Joining strings with a separator isn't always enough to encode data safely.
- Storing the length before each string helps me know exactly how many characters to read.
- Two pointers are useful for moving through an encoded string without decoding it character by character more than necessary.
- The `#` character separates the length from the actual string. It doesn't matter if the original string itself contains `#`, because I use the stored length to find where that string ends.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Test the solution with an empty list and empty strings.
- [ ] Test strings containing `#` and numbers.
- [ ] Explain how the two pointers move during decoding.
- [ ] Explain why the original strings can be recovered exactly.

---

*Another DSA problem completed. I'm learning to think about how data can be represented and recovered, not just how to solve the immediate problem.*
