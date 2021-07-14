n = int(input())
stack = []
oper = []
cnt = 1
ans = True

for i in range(n):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    oper.append('+')
    cnt += 1
  if stack[-1] == num:
    stack.pop()
    oper.append('-')
  else:
    ans = False

if ans == False:
  print('NO')
else:
  for i in oper:
    print(i)