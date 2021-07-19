import sys

string = sys.stdin.readline().rstrip('\n')
arr = []
for i in range(len(string)):
  arr.append(string)
  string = string[1:]

arr.sort()

sys.stdout.write('\n'.join(arr))