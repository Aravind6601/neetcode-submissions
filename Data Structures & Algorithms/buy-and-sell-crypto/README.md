# Best Time to Buy and Sell Stock

**Topic:** Sliding Window  
**Difficulty:** Easy  
**Language:** Python

**Problem:** [Best Time to Buy and Sell Stock — NeetCode](https://neetcode.io/problems/buy-and-sell-crypto)

## My Approach

In this problem, I need to find the maximum profit I can make by buying a stock at one price and selling it later at a higher price.

The important thing is that I have to buy before I sell. I can't just find the highest and lowest prices independently because their order matters.

I used two pointers, `left` and `right`, to keep track of the buying and selling days.

### How I Solved It

1. I started `left` at index `0` and `right` at index `1`.
2. I compared the prices at both pointers.
3. If the price at `right` was higher than the price at `left`, I calculated the profit by subtracting the buying price from the selling price.
4. I updated `max_profit` whenever I found a better profit.
5. If the price at `right` was less than or equal to the price at `left`, I moved `left` to `right`. This gives me a better or equally good buying price for the days ahead.
6. I moved `right` forward and continued until I reached the end of the array.

Finally, I returned `max_profit`. It starts at `0`, so if the prices keep falling and no profitable transaction is possible, the answer stays `0`.

### The Part I Need to Remember

I don't need to check every possible buying and selling pair.

If I find a lower price later, that price is a better option for buying because it gives me more potential profit on future days. That's why I can move `left` forward instead of going back and checking previous prices again.

Also, I must calculate profit only when the selling price is higher than the buying price.

## Time and Space Complexity

Let `n` be the number of days.

- **Time:** `O(n)` — I move through the prices once.
- **Space:** `O(1)` — I only use a few variables to track the pointers and maximum profit.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- The buying day must always come before the selling day.
- A lower buying price can lead to a higher profit later.
- Two pointers help me solve this in one pass instead of checking every possible pair.
- Initializing `max_profit` to `0` handles cases where no profitable transaction exists.
- I should understand why a pointer moves instead of memorizing the code.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Test the solution with prices that keep falling.
- [ ] Test prices with multiple possible buying and selling days.
- [ ] Explain why `left` moves to `right` when the current price is lower or equal.
- [ ] Explain the time and space complexity in my own words.
- [ ] Compare this approach with a brute-force solution.

---

*I'm learning to solve array problems by keeping track of the information I need instead of checking every possible combination.*
