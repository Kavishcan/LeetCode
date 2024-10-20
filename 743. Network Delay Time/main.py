import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Step 1: Build the graph
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Initialize the priority queue and the shortest time dictionary
        pq = [(0, k)]  # (time, node)
        shortest_time = {i: float('inf') for i in range(1, n + 1)}
        shortest_time[k] = 0
        
        # Step 3: Dijkstra's algorithm
        while pq:
            current_time, node = heapq.heappop(pq)
            
            if current_time > shortest_time[node]:
                continue
            
            for neighbor, travel_time in graph[node]:
                time = current_time + travel_time
                if time < shortest_time[neighbor]:
                    shortest_time[neighbor] = time
                    heapq.heappush(pq, (time, neighbor))
        
        # Step 4: Check the results
        max_time = max(shortest_time.values())
        return max_time if max_time < float('inf') else -1
