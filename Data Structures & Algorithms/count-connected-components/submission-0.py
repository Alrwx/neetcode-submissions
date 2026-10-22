class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #make an adj list
        adj = {i: [] for i in range(n)}
        #populate it
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()

        #some type of dfs since we're couting the connected parts
        def dfs(node):
            #ensure node is unique
            if node in visited:
                return
            #add the node so it doesn't get double counted
            visited.add(node)

            #go down the line on the adj list of that specific node
            #theyre all connected if it contains it
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        components = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1


        # print(visited)
        return components

        