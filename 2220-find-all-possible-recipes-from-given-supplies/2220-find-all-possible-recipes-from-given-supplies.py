class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        from collections import defaultdict

        adj = defaultdict(list)
        avail = set(supplies)
        memo = {}

        def dfs(curr):
            if curr in avail: return True
            if curr in memo: return memo[curr]
            if curr not in adj: return False

            memo[curr] = False  # Assume we can't make it
            for ing in adj[curr]:
                if not dfs(ing):
                    return False
            
            avail.add(curr)  # Now we can cook this
            memo[curr] = True
            return True
        
        # Create graph
        for r, ing in zip(recipes, ingredients):
            adj[r] = ing
        
        return [r for r in recipes if dfs(r)]