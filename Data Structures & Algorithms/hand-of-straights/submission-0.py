class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)

        while freq:
            curr = min(freq.keys())
            length = 0
            while curr+length in freq:
                freq[curr+length] -=1
                if freq[curr+length] == 0:
                    del freq[curr+length]
                length+=1
                if length == groupSize:
                    break
            if length != groupSize:
                return False
        return True


    