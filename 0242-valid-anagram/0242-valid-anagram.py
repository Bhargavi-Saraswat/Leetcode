class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                freq[ch] = freq.get(ch,0)+1
        for ch in t:
            if ch.isalpha() or ch.isdigit():
                if ch not in freq:
                    return False
                else:
                    freq[ch] = freq.get(ch) - 1
            if freq[ch] == 0:
                freq.pop(ch)
        if len(freq) == 0:
            return True
        return False