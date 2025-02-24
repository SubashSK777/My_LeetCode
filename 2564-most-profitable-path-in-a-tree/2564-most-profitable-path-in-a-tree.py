class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        depth = [0] * n
        q = deque([0])
        parent[0] = 0
        while q:
            u = q.popleft()
            for v in tree[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
        
        # Compute Bob's arrival times on his path from bob to root.
        bobTime = [float('inf')] * n
        t = 0
        cur = bob
        while True:
            bobTime[cur] = t
            if cur == 0:
                break
            cur = parent[cur]
            t += 1
        
        res = -float('inf')
        def dfs(u: int, t: int, currProfit: int, par: int) -> None:
            nonlocal res
            # If Alice arrives before Bob, she gets full profit; if at the same time, she gets half; if after, she gets nothing.
            if t < bobTime[u]:
                currProfit += amount[u]
            elif t == bobTime[u]:
                currProfit += amount[u] // 2
            # Else, Bob has taken the profit (i.e. add nothing).
            isLeaf = True
            for v in tree[u]:
                if v == par:
                    continue
                isLeaf = False
                dfs(v, t + 1, currProfit, u)
            if isLeaf:
                res = max(res, currProfit)
        
        dfs(0, 0, 0, -1)
        return res