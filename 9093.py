import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
  sentence = list(input().split())
  for i in range(len(sentence)):
    print(sentence[i][::-1], end=' ')
  print()