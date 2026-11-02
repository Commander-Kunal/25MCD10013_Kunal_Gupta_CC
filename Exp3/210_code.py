from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph and calculate in-degrees
        # prerequisites[i] = [ai, bi] means bi -> ai
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
            
        # Add all courses with 0 prerequisites to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            
            # Reduce in-degree for neighboring courses
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we successfully processed all courses, return the order, else empty list (cycle detected)
        return result if len(result) == numCourses else []
