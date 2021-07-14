import sys

string = sys.stdin.readline().rstrip('\n')
num = 0
result = 0

for i in range(len(string)):
  if string[i] == '(':
    num += 1
  elif string[i] == ')':
    num -= 1
    if string[i-1] == '(':
      result += num
    else:
      result += 1

print(result)