import heapq

class Solution:
    def maximumScore(self, nums, k):
        mod = 10**9 + 7

        # Step 1: Implement sieve algorithm to find smallest prime factors
        max_num = max(nums)
        spf = list(range(max_num + 1))
        for i in range(2, int(max_num**0.5) + 1):
            if spf[i] == i:  # i is prime
                for j in range(i*i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Step 2: Calculate prime score for each number
        def get_prime_score(x):
            if x == 1:
                return 0
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x = x // spf[x]
            return len(factors)

        prime_scores = [get_prime_score(num) for num in nums]

        # Step 3: Find subarray counts using monotonic stacks
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Find next greater element to the left
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        # Find next greater or equal element to the right
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Calculate counts for each element
        counts = [(right[i] - i) * (i - left[i]) for i in range(n)]

        # Step 4: Use max-heap to select top elements
        # Implement max-heap using min-heap with negative values
        heap = []
        for i in range(n):
            heapq.heappush(heap, (-nums[i], counts[i]))

        result = 1
        while k > 0 and heap:
            num, cnt = heapq.heappop(heap)
            current_num = -num
            use = min(cnt, k)
            result = (result * pow(current_num, use, mod)) % mod
            k -= use

        return result

# \U0001f680\U0001f525 Keep coding and stay awesome!