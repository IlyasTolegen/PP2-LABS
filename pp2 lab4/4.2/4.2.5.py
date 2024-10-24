def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter the number: "))
for num in countdown(n):
    print(num)
