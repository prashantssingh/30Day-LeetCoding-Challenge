# PROBLEM DESCRIPTION:
# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.
# 
# EXAMPLES:
# 
# INPUT:                                        OUTPUT:
# arr = [1,2,3]                                 2
# EXPLANATION: 1 and 2 are counted cause 2 and 3 are in arr.
# 
# INPUT:                                        OUTPUT:
# arr = [1,1,3,3,5,5,7,7]                       0
# EXPLANATION: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.
# 
# INPUT:                                        OUTPUT:
# arr = [1,3,2,3,5,0]                           3
# EXPLANATION: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

# INPUT:                                        OUTPUT:
# arr = [1,1,2,2]                               2
# EXPLANATION: Two 1s are counted cause 2 is in arr.
# 
# CONSTRAINTS:
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        if not arr: 
            return 0
        
        freq_dict = Counter(arr)
        count = 0
        for key in freq_dict:
            if key+1 in freq_dict:
                # imagine a case - [2,2,3], this should yield 2, as for
                # both x=2, there is x+1=3,
                if freq_dict[key] > freq_dict[key+1]:
                    count += freq_dict[key]
                else:
                    # imagine a case - [2,3,3], as there is only one 2,
                    # one 3 will go unpaired
                    count += min(freq_dict[key], freq_dict[key+1])
                
        return count