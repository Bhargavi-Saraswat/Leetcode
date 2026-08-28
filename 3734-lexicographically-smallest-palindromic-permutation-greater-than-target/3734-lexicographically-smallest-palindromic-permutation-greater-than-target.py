class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        if sum(x % 2 for x in freq) > 1:
            return ""

        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + 97)
                break

        m = n // 2
        cnt = [x // 2 for x in freq]

        def make_pal(h):
            left = ''.join(h)
            return left + mid + left[::-1]

        half = []
        remaining = cnt[:]
        fail = -1

        for i in range(m):
            c = ord(target[i]) - 97

            if remaining[c] > 0:
                half.append(chr(c + 97))
                remaining[c] -= 1
            else:
                fail = i
                break

        if fail == -1:
            candidate = make_pal(half)

            if candidate > target:
                return candidate

            for i in range(m - 1, -1, -1):
                cur = ord(half[i]) - 97
                remaining[cur] += 1

                for c in range(cur + 1, 26):
                    if remaining[c] > 0:
                        new_half = half[:i] + [chr(c + 97)]
                        remaining[c] -= 1

                        for x in range(26):
                            new_half += [chr(x + 97)] * remaining[x]

                        return make_pal(new_half)

            return ""

        for c in range(ord(target[fail]) - 96, 26):
            if remaining[c] > 0:
                new_half = half + [chr(c + 97)]
                remaining[c] -= 1

                for x in range(26):
                    new_half += [chr(x + 97)] * remaining[x]

                return make_pal(new_half)

        for i in range(fail - 1, -1, -1):
            cur = ord(half[i]) - 97
            remaining[cur] += 1

            for c in range(cur + 1, 26):
                if remaining[c] > 0:
                    new_half = half[:i] + [chr(c + 97)]
                    remaining[c] -= 1

                    for x in range(26):
                        new_half += [chr(x + 97)] * remaining[x]

                    return make_pal(new_half)

        return ""