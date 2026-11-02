from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        # Build the adjacency list
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
            
        # BFS to traverse the connected component containing city 1
        visited = set([1])
        queue = deque([1])
        min_score = float('inf')
        
        while queue:
            curr = queue.popleft()
            for neighbor, dist in graph[curr]:
                # Track the minimum distance of any edge connected to this component
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
