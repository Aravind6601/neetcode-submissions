

# Linked List Cycle Detection

## Problem Details
- **Difficulty:** Easy
- **Topic:** Linked List, Two Pointers
- **Problem:** [Linked List Cycle Detection](https://leetcode.com/problems/linked-list-cycle/)

## My Approach

I used the **Slow and Fast Pointer** technique (Floyd's Cycle Detection Algorithm).

Instead of storing visited nodes in a set, I used two pointers to detect whether a cycle exists.

## How I Solved It

1. Initially, both `slow` and `fast` point to the head.
2. Move `slow` one step at a time.
3. Move `fast` two steps at a time.
4. If there is a cycle, the fast pointer will eventually meet the slow pointer.
5. If `fast` or `fast.next` becomes `None`, the list has no cycle.

- If both pointers meet, return `True`.
- If the loop ends, return `False`.

## Time Complexity
**O(n)** – In the worst case, we may need to traverse the linked list to detect the cycle.

## Space Complexity
**O(1)** – Only two pointers are used. No extra data structure is needed.

## What I Learned
- How to use two pointers in a linked list.
- How the fast and slow pointer technique detects cycles.
- Why moving one pointer two steps and the other one step helps them meet inside a cycle.
- How to solve this problem without using extra memory.

## Revision Checklist
- [ ] Understand the slow and fast pointer technique.
- [ ] Know why `while fast and fast.next` is used.
- [ ] Understand why both pointers meet when a cycle exists.
- [ ] Be able to implement the solution without looking at notes.

