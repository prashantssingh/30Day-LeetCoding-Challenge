# PROBLEM DESCRIPTION:
# Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.
# 
# EXAMPLE:
# INPUT:                                                        OUTPUT: 
# S = "ab#c", T = "ad#c"                                        true
# EXPLANATION: Both S and T become "ac".
# 
# INPUT:                                                        OUTPUT: 
# S = "ab##", T = "c#d#"                                        true
# EXPLANATION: Both S and T become "".
# 
# INPUT:                                                        OUTPUT: 
# S = "a##c", T = "#a#c"
# EXPLANATION: Both S and T become "c".
# 
# INPUT:                                                        OUTPUT: 
# S = "a#c", T = "b"                                            false
# EXPLANATION: S becomes "c" while T becomes "b".
# 
# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# FOLLOW UP:
# Can you solve it in O(N) time and O(1) space?

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = list()
        for ch in S:
            if ch == "#" and len(s) > 0:
                s.pop()
            elif ch.isalpha():
                s.append(ch)

        S = ("").join(s)
        
        s = list()
        for ch in T:
            if ch == "#" and len(s) > 0:
                s.pop()
            elif ch.isalpha():
                s.append(ch)

        T = ("").join(s)
                    
        return S == T