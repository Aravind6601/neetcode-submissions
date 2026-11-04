# Search a 2D Matrix

**Topic:** Binary Search  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Search a 2D Matrix — NeetCode](https://neetcode.io/problems/search-2d-matrix)

## My Approach

In this problem, I need to search for a target value in a 2D matrix and return `True` if it exists, otherwise `False`.

The interesting part is that the matrix is sorted in a specific way:
- Each row is sorted in ascending order.
- The first element of each row is greater than the last element of the previous row.

Because of this, I realised that I don't need to search each row separately. I can treat the entire matrix as a single sorted array and apply **Binary Search**.

### How I Solved It

Instead of converting the matrix into a new 1D array, I used the original matrix and calculated the corresponding row and column whenever I needed to access an element.

1. First, I checked whether the matrix or its first row was empty. If so, I returned `False`.
2. I stored the number of rows in `m` and the number of columns in `n`.
3. I initialized `left = 0` and `right = (m * n) - 1`. These represent the first and last positions if the matrix were flattened.
4. I calculated the middle index using `(left + right) // 2`.
5. To access the actual matrix element, I converted the middle index into row and column positions:
   - Row = `mid // n`
   - Column = `mid % n`
6. If the middle element matched the target, I returned `True`.
7. If it was smaller than the target, I moved `left` to `mid + 1`.
8. Otherwise, I moved `right` to `mid - 1`.
9. If the search range became empty, I returned `False`.

### The Part I Need to Remember

The most interesting part of my solution is:

`matrix[mid // n][mid % n]`

I don't actually create a separate 1D array. I just imagine the matrix as one continuous sorted array and use these calculations to access the correct element.

For example, consider this matrix:

```python
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
```

There are 3 rows and 4 columns, so the total number of elements is 12.

If my flattened middle index is `5`:

- Row = `5 // 4 = 1`
- Column = `5 % 4 = 1`
- Element = `matrix[1][1] = 11`

This conversion is what allows me to perform normal binary search directly on a 2D matrix.

## Time and Space Complexity

Let:
- `m` = number of rows
- `n` = number of columns

- **Time:** `O(log(m × n))` — binary search reduces the search space by half in every iteration.
- **Space:** `O(1)` — I don't create another array or use any additional data structure. I only use a few variables.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A sorted 2D matrix can sometimes be treated as a single sorted 1D array.
- Binary Search can be applied to a 2D matrix without actually flattening it.
- Integer division (`//`) helps identify the row, while modulo (`%`) helps identify the column.
- I can avoid using extra memory by calculating the matrix position whenever I need an element.
- Understanding how to map a 1D index to a 2D position is the key idea in this problem.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why `right` is initialized to `(m * n) - 1`.
- [ ] Practise converting different 1D indices into row and column positions.
- [ ] Explain why `mid // n` gives the row.
- [ ] Explain why `mid % n` gives the column.
- [ ] Test cases where the target is the first element, last element, and not present.
- [ ] Explain why the time complexity is `O(log(m × n))`.
- [ ] Try implementing the solution again from scratch.

---

*I'm learning how binary search can be extended beyond normal arrays. The important thing I want to remember is how to search a 2D matrix without actually converting it into a 1D array.*
