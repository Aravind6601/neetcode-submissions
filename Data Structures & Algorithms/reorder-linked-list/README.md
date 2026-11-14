Reorder Linked List
Problem Details
- Topic: Linked List
- Difficulty: Medium
- Language: Python
- Problem: Reorder Linked
  List
My Approach
I solved this by breaking the problem into three steps:
1. Find the middle of the linked list using slow and fast pointers.
2. Reverse the second half of the list.
3. Merge both halves by taking one node from each half alternately.
The main idea is to rearrange the existing nodes in-place instead of
creating a new list or storing them in an array.
How I Solved It
1. Find the middle
I initialize both slow and fast at head.
- slow moves one node at a time.
- fast moves two nodes at a time.
When the loop ends, slow is at the middle of the list (or the end of
the first half).

I take slow.next as the start of the second half and set
slow.next = None to separate the two halves.
2. Reverse the second half
I use three pointers:
- prev -- keeps track of the previous node.
- curr -- points to the node I'm currently processing.
- nxt -- saves the next node before I change the link.
For every node, I save the next node, point the current node backwards,
and move the pointers forward. Once the loop finishes, prev points to
the head of the reversed second half.
3. Merge the two halves
I use first for the first half and second for the reversed second
half.

In each iteration:
1. Save first.next in t1.
2. Save second.next in t2.
3. Connect first to second.
4. Connect second to t1.
5. Move both pointers to their saved next nodes.
I continue until all nodes from the second half are inserted.
Dry Run
Input: 1 → 2 → 3 → 4 → 5

  Stage                         Linked list
  Original                      1 → 2 → 3 → 4 → 5
After splitting               1 → 2 → 3
After reversing second half   1 → 2 → 3
After merging                 1 → 5 → 2 → 4 → 3

Output: 1 → 5 → 2 → 4 → 3
The Part I Need to Remember
This problem combines three linked-list techniques:
- Slow and fast pointers to find the middle.
- Reversing a linked list using prev, curr, and nxt.
- Merging two lists by carefully changing their next pointers.
While merging, I must save both next nodes before changing any links.
Otherwise, I can lose access to the remaining part of either list.

Also, slow.next = None is important because it separates the first
half from the second half before reversing it.
Complexity Analysis
- Time Complexity: O(n) --- Finding the middle, reversing the
  second half, and merging the lists each take linear time.
- Space Complexity: O(1) --- I only use a fixed number of
  pointers and modify the list in-place.
My Solution
[View submission-0.py](./submission-0.py)
What I Learned
- Slow and fast pointers can find the middle without counting all the
  nodes.
- I can reverse only a part of a linked list instead of reversing the
  entire list.
- Saving next pointers before changing links prevents losing the
  remaining nodes.
- Combining smaller linked-list techniques can solve a more complex
  reordering problem.
Practice Again
- [ ] Explain how slow and fast pointers find the middle.
- [ ] Dry-run the reversal of the second half.
- [ ] Explain why the two halves must be separated before reversing.
- [ ] Dry-run the merge for both odd- and even-length lists.
- [ ] Write the complete solution again without looking at the code.
Key takeaway: Find the middle, reverse the second half, and merge
both halves alternately --- all in-place.
