from math import ceil
class Solution:
    def __init__(self):
        self.ans = 0
    def minimum_fuel_cost(self, roads, seats):
        adj = [[] for _ in range(len(roads) + 1)]
        n = len(roads)+1
        self.ans = 0
        for a,b in roads:
            adj[a].append(b)
            adj[b].append(a)
        self.solve(adj, seats, 0, -1)
        return self.ans
    
    def solve(self, adj, seats, src, parent):
        people = 1
        for i in adj[src]:
            if i != parent:
                people += self.solve(adj, seats, i, src)
            if src != 0:
                self.ans += ceil(people/seats)
        return people

if __name__ == '__main__':
    solution = Solution()
    roads =  [[0,1],[0,2],[0,3]]
    seats = 5
    result = solution.minimum_fuel_cost(roads, seats)
    print(result)
                