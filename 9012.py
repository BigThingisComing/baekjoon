tc = int(input())

for _ in range(tc):
  data = input()
  stack = []
  yorn = "YES"
  for i in range(len(data)):
    if data[i] == '(':
      stack.append(data[i])
    else:
      if len(stack) == 0:
        yorn = "NO"
        break
      if stack[-1] == '(':
        stack.pop()
      else:
        yorn = "NO"
        break
  
  if len(stack) != 0:
    yorn = "NO"
  print(yorn)