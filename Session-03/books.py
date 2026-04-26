n, t = map(int, input().split())
books = list(map(int, input().split()))

max_books = 0
current_time = 0
left = 0

for right in range(n):
    current_time += books[right]
    while current_time > t:
        current_time -= books[left]
        left += 1
    max_books = max(max_books, right - left + 1)

print(max_books)
