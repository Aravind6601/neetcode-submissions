# Sliding Window Maximum

**Topic:** Sliding Window · Monotonic Queue  
**Difficulty:** Hard  
**Language:** Python

**Problem:** [Sliding Window Maximum — NeetCode](https://neetcode.io/problems/sliding-window-maximum)

## My Approach

In this problem, I need to find the maximum element in every contiguous window of size `k` in the given array.

For example:

- `nums = [1, 3, -1, -3, 5, 3, 6, 7]`
- `k = 3`
- **Output:** `[3, 3, 5, 5, 6, 7]`

The straightforward approach would be to find the maximum element separately for every window, but that would involve repeating a lot of work.

I used a **monotonic deque** to keep track of the useful elements in the current window so I can get the maximum efficiently.

### How I Solved It

I used Python's `deque` from the `collections` module and stored indices instead of actual numbers.

Here's what I did:

1. I created an empty result list called `res` and a deque called `q`.
2. I went through the array using `enumerate()` so I could access both the index and its value.
3. First, I checked whether the index at the front of the deque was outside the current window. If it was, I removed it using `popleft()`.
4. Then I checked the elements at the back of the deque. If their values were smaller than or equal to the current value, I removed them using `pop()`.
5. I added the current index to the deque.
6. Once I had processed at least `k` elements, I added the value at the front of the deque to my result.
7. After going through the entire array, I returned the result.

### The Part I Need to Remember

The most important part of my solution is maintaining the deque in decreasing order of values.

I remove smaller or equal elements from the back because the current element is bigger and comes later in the array. So those smaller elements can never become the maximum while the current element is still inside the window.

I also store indices instead of values because I need to know when an element goes outside the sliding window.

For example, when the window moves forward, an index that is no longer part of the current window must be removed from the front.

That's how I can always get the maximum element directly from `nums[q[0]]` without searching through the entire window again.

## Time and Space Complexity

Let `n` be the number of elements in the array and `k` be the window size.

- **Time:** `O(n)` — every index is added to the deque once and removed at most once. Even though there is a `while` loop, the total number of deque operations is linear.
- **Space:** `O(k)` — the deque stores at most the useful indices from the current window. The result list requires an additional `O(n - k + 1)` space.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A deque allows me to efficiently add and remove elements from both ends.
- A monotonic deque helps maintain elements in decreasing order.
- Storing indices instead of values makes it easier to identify elements that leave the current window.
- Smaller elements can be removed because a bigger element appearing later makes them unnecessary as maximum candidates.
- I don't need to calculate the maximum from scratch for every window.
- The total number of deque operations remains linear, which gives me O(n) time complexity.

## Practice Again

- [ ] Solve this problem again without looking at my code.
- [ ] Understand why I store indices instead of actual values.
- [ ] Trace the deque for `[1, 3, -1, -3, 5]` with `k = 3`.
- [ ] Explain why smaller elements are removed from the back.
- [ ] Understand why expired indices are removed from the front.
- [ ] Explain why the deque front always represents the maximum of the current window.
- [ ] Explain why the solution takes O(n) time even though it contains a `while` loop.
- [ ] Try implementing the solution again using `deque` without referring to my previous code.

---

*I'm learning that choosing the right data structure can eliminate repeated work. The monotonic deque is the important pattern I want to remember from this problem.*
