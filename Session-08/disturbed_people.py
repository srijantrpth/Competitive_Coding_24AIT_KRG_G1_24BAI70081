n = int(input())
a = list(map(int, input().split()))
count = 0
i = 1
while i < n - 1:
    if a[i-1] == 1 and a[i] == 0 and a[i+1] == 1:
        count += 1
        i += 2 # Skip ahead to avoid double counting
    i += 1
print(count)
