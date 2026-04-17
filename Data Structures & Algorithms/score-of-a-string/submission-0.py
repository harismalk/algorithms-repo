class Solution:
    def scoreOfString(self, s: str) -> int:
        
        '''
        c o d e
        99 111 100 101
        
        111 - 99
        100 - 111
        101 - 100
        '''

        res = 0

        for i in range(len(s)-1):
            curr = ord(s[i])
            right = ord(s[i+1])
            res+= abs(curr-right)
        return res
