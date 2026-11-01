class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Build frequency map for t manually (no imports needed)
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have, need = 0, len(count_t)
        res = [-1, -1]
        res_len = float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Contract from left while window remains valid
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Shrink window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""