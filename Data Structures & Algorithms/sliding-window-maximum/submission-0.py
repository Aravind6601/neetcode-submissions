from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i, val in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] <= val:
                q.pop()
            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
        