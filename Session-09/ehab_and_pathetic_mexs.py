import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
edges = []
for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(i)
    adj[v].append(i)
    edges.append(-1)

res = [-1] * (n - 1)
curr = 0
# Find a node with at least 3 edges
for i in range(1, n + 1):
    if len(adj[i]) >= 3:
        for edge_idx in adj[i]:
            res[edge_idx] = curr
            curr += 1
        break

for i in range(n - 1):
    if res[i] == -1:
        res[i] = curr
        curr += 1
    print(res[i])
