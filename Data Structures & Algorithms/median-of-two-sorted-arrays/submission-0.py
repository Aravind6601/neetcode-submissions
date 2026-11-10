class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2   
            j = half - i              

            A_left = A[i - 1] if i > 0 else float("-infinity")
            A_right = A[i] if i < m else float("infinity")
            B_left = B[j - 1] if j > 0 else float("-infinity")
            B_right = B[j] if j < n else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 != 0:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1