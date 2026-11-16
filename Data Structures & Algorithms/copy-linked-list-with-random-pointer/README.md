# Copy Linked List with Random Pointer

## Problem Details
- **Difficulty:** Medium
- **Topics:** Linked List, Hashing
- **Platform:** [LeetCode – Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

## My Approach

I solved this using the **Interweaving Linked List approach** without using an extra HashMap.

Instead of creating a separate mapping between original and copied nodes, I insert each copied node right after its original node. This makes it easy to connect the `random` pointers.

## How I Solved It

I divided the solution into 3 passes:

### 1. Create and Insert Copy Nodes
- Traverse the original linked list.
- Create a new node with the same value.
- Insert it immediately after the original node.
- Now every original node is followed by its copy.

### 2. Assign Random Pointers
- Traverse the list again.
- If an original node has a random pointer, assign the copy's random pointer using:

  `curr.next.random = curr.random.next`

- Since every copied node is placed after its original node, `curr.random.next` gives the copied version of the random target.

### 3. Separate Both Lists
- Store the first copied node in `copy_head`.
- Restore the original list by skipping copied nodes.
- Connect copied nodes to their next copied nodes.
- Finally, return `copy_head`.

## Complexity Analysis

- **Time Complexity:** O(n) – Three traversals of the linked list.
- **Space Complexity:** O(1) – No extra HashMap or array is used. The copied nodes are part of the output.

## What I Learned

- How to clone a linked list without an extra HashMap.
- How interweaving original and copied nodes makes random pointer connections easier.
- Why the order of the three passes is important.
- How to restore the original linked list while extracting the copied list.

## Revision Checklist

- [ ] Understand why copied nodes are inserted after original nodes.
- [ ] Remember how `curr.random.next` identifies the copied random node.
- [ ] Be able to separate both linked lists without losing connections.
- [ ] Explain why the solution uses O(1) auxiliary space.
