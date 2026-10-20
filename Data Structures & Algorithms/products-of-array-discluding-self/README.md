# Product of Array Except Self

**Topic:** Arrays & Hashing  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Product of Array Except Self — NeetCode](https://neetcode.io/problems/products-of-array-discluding-self)

## My Approach

In this problem, I need to return an array where each element is the product of all the numbers in the original array except the number at that same position.

The interesting part is that I can't use division, so I need another way to calculate the products efficiently.

I used the **prefix and postfix product** approach. Instead of calculating the product separately for every element, I calculate the products from the left side and the right side.

### How I Solved It

I created a result array filled with `1` and used two passes.

**First pass — Prefix product**

I moved from left to right and kept track of the product of all the elements before the current index.

At each position, I stored that prefix product in the result array before multiplying it by the current number.

**Second pass — Postfix product**

Then I moved from right to left and kept track of the product of all the elements after the current index.

At each position, I multiplied the existing result by the postfix product. This gave me the product of everything to the left and everything to the right, excluding the current element.

For example, with `[1, 2, 3, 4]`, the final result is `[24, 12, 8, 6]`.

The best part is that I don't need separate prefix and postfix arrays. I can store the prefix products directly in `res` and multiply them by the postfix products during the second pass.

## Time and Space Complexity

Let `n` be the number of elements in the array.

- **Time:** `O(n)` — I traverse the array twice.
- **Extra space:** `O(1)` auxiliary space, excluding the result array. I only use a couple of variables to keep track of the prefix and postfix products.

The result array itself requires `O(n)` space.

## My Solution

- [View submission-0.py](./submission-0.py)
- [View submission-1.py](./submission-1.py)

Both files currently contain the same solution.

## What I Learned

- Prefix and postfix products can help solve array problems without using division.
- I can solve the problem in two passes instead of repeatedly multiplying all the other elements.
- The result array can be reused to store prefix products, saving the need for an additional array.
- Understanding what each variable represents makes the solution easier to follow.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand what `prefix` and `postfix` represent at each index.
- [ ] Test the solution with zeros and negative numbers.
- [ ] Explain why the current element is excluded from its own product.
- [ ] Explain the time and space complexity in my own words.

---

*Learning DSA one problem at a time. The goal is to understand the pattern so I can recognize it in other problems too.*
