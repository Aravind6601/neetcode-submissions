# Reverse a Linked List

## Problem Details
- **Topic:** Linked List
- **Difficulty:** Easy
- **Language:** Python
- **Problem:** [Reverse a Linked List](https://neetcode.io/problems/reverse-a-linked-list)

## My Approach

I used the **Iterative Two-Pointer Approach**.

The idea is to reverse the direction of each node's `next` pointer instead of creating a new linked list.

I used three pointers:
- `prev` – stores the previous node.
- `curr` – points to the node I'm currently processing.
- `nxt` – temporarily saves the next node so I don't lose the remaining list.

## How I Solved It

Initially:
- `prev = None`
- `curr = head`

For every node, I follow these steps:

1. Store the next node in `nxt`.
2. Change `curr.next` to point to `prev`.
3. Move `prev` to `curr`.
4. Move `curr` to `nxt`.

I repeat this until `curr` becomes `None`.

Finally, `prev` points to the new head of the reversed linked list, so I return it.

### Dry Run

**Input:** `1 → 2 → 3 → None`

| Step | prev | curr | Action |
|---|---|---|---|
| Start | None | 1 | Initialize pointers |
| 1 | 1 | 2 | Reverse 1's link |
| 2 | 2 | 3 | Reverse 2's link |
| 3 | 3 | None | Reverse 3's link |

**Output:** `3 → 2 → 1 → None`

## The Part I Need to Remember

The order of these four operations is important:

```python
nxt = curr.next
curr.next = prev
prev = curr
curr = nxt
```

I must save `curr.next` before reversing the link. Otherwise, I may lose access to the remaining nodes.

## Complexity Analysis

- **Time Complexity:** `O(n)` — Every node is visited exactly once.
- **Space Complexity:** `O(1)` — Only three pointers are used; no extra linked list is created.

## My Solution

[View submission-0.py](./submission-0.py)

## What I Learned

- A linked list consists of nodes connected using pointers.
- `head` points to the first node.
- `next` stores the reference to the following node.
- Reversing a linked list means changing the direction of its links.
- The iterative approach can reverse the list without using extra space.

## Practice Again

- [ ] Explain what a linked list is without looking at notes.
- [ ] Understand the role of `head`, `prev`, `curr`, and `nxt`.
- [ ] Dry-run the code for 1 node, 2 nodes, and 3+ nodes.
- [ ] Write the solution again without looking at the original code.
- [ ] Explain why `nxt = curr.next` must happen before changing the link.

**Key takeaway:** Save the next node, reverse the current link, and move forward. Repeat until the list is reversed.
