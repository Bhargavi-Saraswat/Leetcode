from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: (start, end, weight, original_index)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]

        # Sort by ending position
        arr.sort(key=lambda x: x[1])

        # Ends of sorted intervals
        ends = [x[1] for x in arr]

        # prev[i] = last interval that ends strictly before arr[i] starts
        # bisect_left is required because sharing a boundary means overlapping.
        prev = []
        for i in range(n):
            start = arr[i][0]
            j = bisect_right(ends, start - 1) - 1
            prev.append(j)

        # dp[k][i] = best result using first i intervals
        # with at most k intervals.
        #
        # Store (score, tuple of indices)
        # The tuple is already sorted because we construct it from indices
        # and compare lexicographically when scores are equal.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            """
            Return the better of two states.
            Higher score wins.
            If scores are equal, lexicographically smaller indices win.
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take interval i-1
                best = dp[k][i - 1]

                idx = i - 1
                l, r, w, original_idx = arr[idx]

                # Take interval idx.
                p = prev[idx] + 1

                old_score, old_indices = dp[k - 1][p]

                candidate = (
                    old_score + w,
                    tuple(sorted(old_indices + (original_idx,)))
                )

                best = better(best, candidate)

                dp[k][i] = best

        return list(dp[4][n][1])