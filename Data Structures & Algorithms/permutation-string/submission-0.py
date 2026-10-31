class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        l = 0
        for r in range(n1, n2):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            s2_count[idx] += 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] + 1 == s2_count[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2_count[idx] -= 1
            if s1_count[idx] == s2_count[idx]:
                matches += 1
            elif s1_count[idx] - 1 == s2_count[idx]:
                matches -= 1

            l += 1

        return matches == 26