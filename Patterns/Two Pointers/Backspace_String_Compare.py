class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Time Complexity : O(n + m)
        # Space Complexity : O(1)
        
        def next_valid_char(string: str, i: int) -> int:
            skip = 0
            while i >= 0:
                if string[i] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return i                    # valid char found
                i -= 1
            return -1
        
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            i = next_valid_char(s, i)
            j = next_valid_char(t, j)
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            
            i -= 1
            j -= 1
        
        return True
    
# Time compelxity - BigO(n+m)
# Space Compelxity - BigO(1)