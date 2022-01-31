n = int(input())
list = []
for i in range (n):
    list.append(int(input()))
print(*list, sep = '\n')
print()
for i in list:
    x = i**2 + 2 * i + 1
    print(x)
