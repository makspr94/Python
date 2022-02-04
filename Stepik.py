# n = int(input())
# list = []
# for i in range (n):
#     list.append(int(input()))
# if n > 2:
#     list.remove(max(list))
#     list.remove(min(list))
# print(list)

# s = input()
# words = s.split()
# print(words[0][0], words[1][0], words[2][0], sep = '.')
#


#s = input().split("\\")
#print(*s, sep = '\n')

# numbers = [8, 9, 10, 11]
# del numbers[1]
# numbers.insert(1, 17)
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers.extend(numbers)
# numbers.insert(3,25)
# print(numbers)

s = input().split()
s = [int(x) for x in s]
max_index = s.index(max(s))
min_index = s.index(min(s))
s[max_index], s[min_index] = s[min_index], s[max_index]
# s = [str(x) for x in s]
# s = ' '.join(s)
print(*s)





