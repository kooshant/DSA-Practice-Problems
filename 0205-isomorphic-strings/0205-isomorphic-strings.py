class Solution:
    def isIsomorphic(self, s, t):
        for i in range(len(s)):

            first_s = s.find(s[i])
            first_t = t.find(t[i])

            if first_s != first_t:
                return False

        return True