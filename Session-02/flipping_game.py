n = int(input())
a = list(map(int, input().split()))

count_ones = sum(a)
max_gain = -1
current_gain = 0

for x in a:
    val = 1 if x == 0 else -1
    current_gain += val
    max_gain = max(max_gain, current_gain)
    if current_gain < 0:
        current_gain = 0

print(count_ones + max_gain)
