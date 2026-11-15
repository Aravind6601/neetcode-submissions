# Remove Nth Node From End of Linked List

## Problem Details
- **Difficulty:** Medium
- **Topic:** Linked List, Two Pointers
- **Platform:** [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## My Approach

I used the **Two Pointers** technique with a dummy node.

Instead of calculating the linked list length first, I maintain a gap of `n` nodes between `fast` and `slow`. This helps me find the node just before the one that needs to be removed.

## How I Solved It

1. Created a dummy node and connected it to the head. This handles edge cases like removing the first node.
2. Started both `slow` and `fast` pointers at the dummy node.
3. Moved `fast` forward by `n` steps to create the gap.
4. Moved both pointers one step at a time until `fast` reached the last node.
5. Now `slow` is just before the node to remove.
6. Skipped that node using `slow.next = slow.next.next`.
7. Returned `dummy.next` as the updated head.

## Complexity Analysis

- **Time Complexity:** `O(n)` — I traverse the linked list once.
- **Space Complexity:** `O(1)` — Only two pointers and a dummy node are used.

## What I Learned

- How to use two pointers to solve linked list problems efficiently.
- Maintaining a fixed gap between pointers helps locate a node from the end.
- A dummy node makes edge cases, especially deleting the head, easier to handle.
- I don't always need to calculate the linked list length separately.

## Revision Checklist

- [ ] Understand why the dummy node is needed.
- [ ] Dry-run with `n = 1`.
- [ ] Dry-run when `n` equals the list length.
- [ ] Explain how the gap between `slow` and `fast` works.
- [ ] Implement the solution again without looking at my code.
