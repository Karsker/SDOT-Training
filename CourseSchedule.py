from collections import defaultdict
class Solution:
    def canFinish(self, n, prerequisites):
        G = defaultdict(list)
        degree = [0]*n
        for e in prerequisites:
            G[e[1]].append(e[0])
            degree[e[0]] += 1
        no_prerequisites = set(i for i in range(n) if degree [i] == 0)
        while no_prerequisites:
            course = no_prerequisites.pop()
            for neighbor in G[course]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    no_prerequisites.add(neighbor)
        return int(sum(degree) == 0)

if __name__ == '__main__':
    N, M = map(int, input().split())
    prerequisites = [list(map(int, input().split())) for _ in range(M)]
    Obj = Solution()
    print(Obj.canFinish(N, prerequisites))