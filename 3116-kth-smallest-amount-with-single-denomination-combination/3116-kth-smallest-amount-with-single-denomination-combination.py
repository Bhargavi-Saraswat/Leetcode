class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def count(x):
            n = len(coins)
            ans = 0

            for mask in range(1, 1 << n):

                lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        lcm = lcm // math.gcd(lcm, coins[i]) * coins[i]

                        if lcm > x:
                            break

                if lcm > x:
                    continue

                if bits % 2 == 1:
                    ans += x // lcm
                else:
                    ans -= x // lcm

            return ans

        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left