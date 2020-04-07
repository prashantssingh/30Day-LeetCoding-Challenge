# PROBLEM DESCRIPTION:
# Given an array of strings, group anagrams together.
# 
# EXAMPLE:
# 
# INPUT:                                                        OUTPUT:
# ["eat", "tea", "tan", "ate", "nat", "bat"],                   [
#                                                                   ["ate","eat","tea"],
#                                                                   ["nat","tan"],
#                                                                   ["bat"]
#                                                               ]
# 
# NOTE:
# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: 
            return []
        
        anagram_dict = {}
        for str in strs:
            key = tuple(sorted(list(str)))
            if key in anagram_dict:
                anagram_dict[key].append(str)
            else:
                anagram_dict[key] = [str]
          
        return anagram_dict.values()