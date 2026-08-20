class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        i = 0
        for ch in s:
            if ch.isdigit():
                i = i*10 +int(ch)
            if ch.isalpha():
                curr += ch
            if ch == '[':
                stack.append((i,curr))
                i = 0
                curr = ""
            if ch == ']':
                j,prev = stack.pop()
                curr = prev + curr*j
        return curr
            