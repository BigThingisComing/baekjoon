size = int(input())
array = list(map(int,input().split()))
NGE = [-1 for i in range(size)]
stack = []

for i in range(size):
  while stack and (stack[-1][0] < array[i]):
    num, index = stack.pop()
    NGE[index] = array[i]
  stack.append([array[i], i])

print(' '.join(map(str, NGE)))