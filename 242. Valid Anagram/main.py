from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        # s_dict = {}
        # t_dict = {}
        # for i in range(len(s)):
        #     s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        # for i in range(len(t)):
        #     t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict
