def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n == 2:
        print(-1)
        return
    
    nums = []
    for i in range(1, n*n + 1, 2): nums.append(i)
    for i in range(2, n*n + 1, 2): nums.append(i)
    
    for i in range(n):
        print(*(nums[i*n : (i+1)*n]))

t = int(input())
for _ in range(t):
    solve()

