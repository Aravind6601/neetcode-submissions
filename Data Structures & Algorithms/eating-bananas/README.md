# Koko Eating Bananas

**Topic:** Binary Search  
**Difficulty:** Medium  
**Language:** Python

**Problem:** [Koko Eating Bananas — NeetCode](https://neetcode.io/problems/eating-bananas)

## My Approach

In this problem, Koko has several piles of bananas and a limited number of hours to finish eating them. I need to find the minimum eating speed `k` that allows her to finish all the bananas within `h` hours.

The interesting part is that I don't need to try every possible speed one by one. I used **Binary Search on the Answer** to find the minimum valid speed.

### How I Solved It

I used two variables, `left` and `right`, to define the possible eating speeds.

1. I initialized `left = 1` because Koko must eat at least one banana per hour.
2. I set `right = max(piles)` because eating at the speed of the largest pile allows her to finish each pile in one hour.
3. I calculated the middle speed using `(left + right) // 2`.
4. For that speed, I calculated how many hours Koko would need to finish all the piles.
5. I used `(p + mid - 1) // mid` to calculate the hours required for each pile. This performs ceiling division because even one remaining banana requires another hour.
6. If the total hours were less than or equal to `h`, the speed was sufficient. So I moved `right` to `mid` to check whether a slower speed could also work.
7. If the required hours were greater than `h`, the speed was too slow. So I moved `left` to `mid + 1`.
8. I continued until both pointers met and returned `left`.

### The Part I Need to Remember

The most important part of this solution is understanding why I can apply binary search to the eating speed.

If Koko can finish all the bananas at a particular speed, she can also finish them at any higher speed.

For example, consider:

- `piles = [3, 6, 7, 11]`
- `h = 8`

At an eating speed of `4`:

- First pile: 1 hour
- Second pile: 2 hours
- Third pile: 2 hours
- Fourth pile: 3 hours

Total = 8 hours.

So speed `4` is valid.

This gives me a monotonic condition: slower speeds might fail, while sufficiently faster speeds will work.

That's why I can discard half of the possible speeds after every binary search iteration.

One more thing I need to remember is:

`(p + mid - 1) // mid`

This is how I calculate the ceiling of `p / mid` using integer division.

## Time and Space Complexity

Let:
- `n` = number of banana piles
- `m` = maximum number of bananas in a pile

- **Time:** `O(n log m)` — binary search takes `O(log m)` iterations, and calculating the hours for each speed requires traversing all `n` piles.
- **Space:** `O(1)` — I only use a few variables and don't create any additional data structures.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Binary Search can be used to find the minimum valid answer, not just search for an element in an array.
- When a condition is monotonic, I can eliminate half of the search space.
- Ceiling division helps calculate the required hours correctly.
- If a particular speed works, higher speeds will also work.
- Moving `right` to `mid` instead of `mid - 1` is important because the current speed might already be the minimum valid answer.
- Understanding the feasible and infeasible conditions is the key to solving this type of binary search problem.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why the search range starts at `1` and ends at `max(piles)`.
- [ ] Explain how `(p + mid - 1) // mid` works.
- [ ] Trace the binary search using `[3, 6, 7, 11]` with `h = 8`.
- [ ] Explain why a higher eating speed can never increase the required hours.
- [ ] Understand why I use `right = mid` when the speed is valid.
- [ ] Explain why the time complexity is `O(n log m)`.
- [ ] Try implementing the solution again from scratch.

---

*I'm learning that binary search isn't limited to sorted arrays. Whenever I can identify a monotonic condition, I can use binary search to find the minimum or maximum answer efficiently.*
