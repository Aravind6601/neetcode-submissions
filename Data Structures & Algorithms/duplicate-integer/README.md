# Contains Duplicate

**Topic:** Arrays & Hashing  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Contains Duplicate — NeetCode](https://neetcode.io/problems/duplicate-integer)

## My Approach

The problem is simple: I need to check whether any number appears more than once in the given array.

I tried two approaches for this problem.

### Approach 1: Using a Set

My first approach was to create an empty set called `seen` and go through the array one number at a time.

- If the number is already present in the set, I return `True`.
- Otherwise, I add that number to the set.
- If I finish checking all the numbers without finding a duplicate, I return `False`.

**Solution:** [View submission-0.py](./submission-0.py)

### Approach 2: Comparing Lengths

In my second approach, I used a simple idea: a set only stores unique values.

For example, `[1, 2, 3, 2]` has 4 elements, but `set([1, 2, 3, 2])` contains only 3 unique elements.

So I compared the length of the original array with the length of its set.

```python
return len(nums) != len(set(nums))
```

If the lengths are different, a duplicate exists. Otherwise, all the numbers are unique.

**Solution:** [View submission-1.py](./submission-1.py)

## Time and Space Complexity

| Approach | Time | Space |
|---|---|---|
| Using a set and loop | O(n) average | O(n) |
| Comparing lengths | O(n) average | O(n) |

Here, `n` is the number of elements in the array.

## What I Learned

- A set stores only unique elements.
- Sets are useful when I need to check whether an element already exists.
- I can solve some problems with a simple property of a data structure instead of writing extra loops.
- The first approach can stop immediately when it finds a duplicate, while the second approach is shorter to write.

## Practice Again

- [ ] Solve this problem without looking at my previous solutions.
- [ ] Explain why a set removes duplicates.
- [ ] Compare both approaches in an interview.
- [ ] Try solving it using sorting.

---

*DSA practice — learning one problem and one concept at a time.*
