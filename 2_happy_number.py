# PROBLEM DESCRIPTION:
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the process until the 
# number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.
# 
# EXAMPLE: 
# INPUT:                            OUTPUT:
# 19                                true
# 
# EXPLANATION: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        if not n: return False
        
        happy_num_dict = dict()
        while True:
            print(n)
            if n in happy_num_dict:
                return False
            happy_num_dict[n] = sum([int(i)**2 for i in list(str(n))])
            n = happy_num_dict[n]
            if n == 1:
                return True