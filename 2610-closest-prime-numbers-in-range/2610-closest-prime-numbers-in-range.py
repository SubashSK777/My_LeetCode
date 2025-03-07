class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Use Sieve of Eratosthenes to find all prime numbers up to `right`
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

        for i in range(2, int(right**0.5) + 1):  # Iterate only up to sqrt(right)
            if is_prime[i]:
                for j in range(i * i, right + 1, i):  # Start marking from i*i
                    is_prime[j] = False

        # Step 2: Collect primes in the given range
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: Find the closest pair
        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair