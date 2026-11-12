# Merge Two Sorted Linked Lists

## Problem Details
- **Problem:** Merge Two Sorted Linked Lists
- **Difficulty:** Easy
- **Topic:** Linked List, Two Pointers
- **Problem Link:** [NeetCode - Merge Two Sorted Linked Lists](https://neetcode.io/problems/merge-two-sorted-linked-lists)

## My Approach

I used a **Dummy Node** to build the merged linked list without creating new nodes.

First, I created a dummy node and kept a `curr` pointer to track where the next node should be attached.

- I compared the values of both lists.
- If `list1.val` was smaller or equal, I connected that node to `curr.next` and moved `list1`.
- Otherwise, I connected the node from `list2` and moved `list2`.
- After every connection, I moved `curr` forward.

The loop continues until one of the lists becomes empty. At that point, I connect the remaining part of the other list directly using:

`curr.next = list1 or list2`

Finally, I return `dummy.next` because the dummy node itself is not part of the answer.

## Time Complexity
**O(n + m)** – Each node from both linked lists is visited only once.

## Space Complexity
**O(1)** – I reused the existing nodes instead of creating a new linked list.

## My Solution
[Python Solution](submission-0.py)

## What I Learned
- How to merge two sorted linked lists using pointers.
- Why a dummy node makes linked-list construction easier.
- How to connect the remaining nodes without traversing them again.
- How to reuse existing nodes instead of allocating extra memory.

## Revision Checklist
- [ ] Can I explain why we use a dummy node?
- [ ] Can I merge two sorted lists without creating new nodes?
- [ ] Do I understand why `dummy.next` is returned?
- [ ] Can I explain how the remaining nodes are attached?
