# Reorder Linked List

## Problem Details
- **Problem:** Reorder Linked List
- **Difficulty:** Medium
- **Topic:** Linked List
- **Language:** Python
- **Problem Link:** [NeetCode – Reorder Linked List](https://neetcode.io/problems/reorder-linked-list)

## My Approach

I used three steps to solve this problem:

1. **Find the middle:** Use slow and fast pointers to reach the middle of the linked list.
2. **Reverse the second half:** Disconnect the list at the middle and reverse the remaining nodes.
3. **Merge both halves:** Connect nodes alternately, taking one from the first half and one from the reversed second half.

This way, I can reorder the list without creating another linked list.

## Time Complexity
- **O(n)** – Finding the middle, reversing the second half, and merging both halves each take linear time.

## Space Complexity
- **O(1)** – Everything is done by changing pointers. No extra data structure is used.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- Slow and fast pointers can help find the middle of a linked list in one traversal.
- Reversing a linked list can be done by changing the `next` pointers.
- Before merging, I need to save the next nodes (`t1` and `t2`) so I don't lose the remaining parts of either list.
- Combining multiple linked-list techniques can solve a problem without using extra space.

## Revision Checklist

- [ ] Find the middle using slow and fast pointers.
- [ ] Reverse the second half of a linked list.
- [ ] Merge two linked lists alternately.
- [ ] Solve the problem again without looking at the code.
