from collections import defaultdict


class Solution(object):
    def groupAnagrams1(self, strs):
        anagrams_dict = defaultdict(list)
        for s in strs:
            # using the sorted_word as the key because strings are immutable
            sorted_word = ''.join(sorted(s))
            anagrams_dict[sorted_word].append(s)

        return anagrams_dict.values()

    def groupAnagrams2(self, strs):
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return anagrams_dict.values()
