class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = Counter(t), {}
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("INF")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1

            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
            
                window[s[l]]-=1
                if countT[s[l]] > window[s[l]]:
                    have-=1
                l+=1
        l, r = res

        return s[l:r+1] if resLen != float("INF") else ""


            