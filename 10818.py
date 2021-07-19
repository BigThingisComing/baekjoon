in_num = int(input())

min_num = 1000001
max_num = -1000001

num = list(map(int, input().split()))

for i in range(len(num)):
  if min_num > num[i]:
    min_num = num[i]
  if max_num < num[i]:
    max_num = num[i]

print(min_num, max_num)