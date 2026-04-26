def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    k = 0
    while k < n - 1 and a[k] == 1:
        k += 1
    
    # If the number of leading '1's is even, First player wins
    # unless all are 1s, then it depends on n.
    if k % 2 == 0:
        print("First")
    else:
        print("Second")

t = int(input())
for _ in range(t):
    solve()
