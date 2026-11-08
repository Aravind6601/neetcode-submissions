# Time Based Key-Value Store

**Topic:** Binary Search / Design  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Time Based Key-Value Store — NeetCode](https://neetcode.io/problems/time-based-key-value-store)

## My Approach

In this problem, I need to design a data structure that stores multiple values for the same key, each associated with a timestamp.

There are two operations:

- `set(key, value, timestamp)` – Store a key-value pair with its timestamp.
- `get(key, timestamp)` – Return the value associated with the largest timestamp that is less than or equal to the given timestamp.

I used a **Dictionary + Binary Search** approach.

I used a dictionary to store each key along with a list of its timestamp-value pairs. Since the timestamps are provided in increasing order, I can use Binary Search to find the required value efficiently.

### How I Solved It

1. In `__init__`, I created an empty dictionary called `store`.
2. In `set()`, I checked whether the key already exists.
   - If it doesn't exist, I created an empty list for that key.
   - Then I appended `(timestamp, value)` to its list.
3. In `get()`, I first checked whether the key exists.
   - If it doesn't exist, I returned an empty string.
4. I initialized two pointers, `l` and `r`, to perform Binary Search on that key's list.
5. I created an `ans` variable initialized to an empty string.
6. During Binary Search:
   - If `arr[mid][0] <= timestamp`, I found a valid timestamp.
   - I stored its corresponding value in `ans`.
   - Then I moved `l = mid + 1` to search for a potentially better timestamp.
   - Otherwise, I moved `r = mid - 1`.
7. Finally, I returned `ans`.

### The Part I Need to Remember

The most important condition is:

`arr[mid][0] <= timestamp`

I need the largest timestamp that does not exceed the requested timestamp.

Whenever this condition is true, I store the current value and continue searching on the right side.

This is slightly different from normal Binary Search because I am not simply searching for an exact match. I am searching for the **rightmost valid timestamp**.

## Time and Space Complexity

Let `n` be the number of stored timestamp-value pairs for a particular key.

- **set():** `O(1)` amortized – Dictionary insertion and list append take constant time on average.
- **get():** `O(log n)` – Binary Search eliminates half of the search range in every iteration.
- **Space:** `O(N)` – The dictionary stores all keys and their timestamp-value pairs, where `N` is the total number of stored entries.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A dictionary can store multiple values for each key using a list.
- Binary Search can find the closest valid timestamp efficiently.
- I don't always need an exact match in Binary Search.
- Moving `l = mid + 1` helps me find the rightmost valid timestamp.
- Initializing `ans` with an empty string handles cases where no valid timestamp exists.
- This problem helped me understand how Binary Search can be combined with other data structures.

## Practice Again

- [ ] Implement the `TimeMap` class without looking at my code.
- [ ] Understand why I used a dictionary.
- [ ] Understand why each key stores a list of timestamp-value pairs.
- [ ] Remember why Binary Search is better than linear search here.
- [ ] Dry-run a case where the exact timestamp exists.
- [ ] Dry-run a case where the requested timestamp falls between two timestamps.
- [ ] Test a timestamp smaller than all stored timestamps.
- [ ] Test a key that does not exist.
- [ ] Explain why `get()` takes `O(log n)` time.
- [ ] Implement the solution from scratch.

---

*I'm learning how to combine dictionaries with Binary Search. The main thing I want to remember is that I need the rightmost timestamp that is less than or equal to the requested timestamp, not necessarily an exact match.*
