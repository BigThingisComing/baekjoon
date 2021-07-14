from sys import stdin
from collections import Counter

size = int(stdin.readline())
array = list(stdin.readline().split())
cnt = Counter(array)

array = [[cnt[num], int(num)] for num in array]
NGF = [-1 for _ in range(size)]

stack = []

stack.append(0)

for i in range(1, size):
  while stack and array[stack[-1]][0] < array[i][0]:
    NGF[stack[-1]] = array[i][1]
    stack.pop()
  
  stack.append(i)

print(' '.join(map(str, NGF)))