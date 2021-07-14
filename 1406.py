import sys
input = sys.stdin.readline

sent_l = list(input().rstrip())
sent_r = []
com_cnt = int(input())

for _ in range(com_cnt):
  command = input()
  if command[0] == 'L' and len(sent_l) > 0:
    sent_r.append(sent_l.pop())
  elif command[0] == 'D' and len(sent_r) > 0:
    sent_l.append(sent_r.pop())
  elif command[0] == 'B' and len(sent_l) > 0:
    sent_l.pop()
  elif command[0] == 'P':
    sent_l.append(command[2])

sent_l.extend(sent_r[::-1])

print(''.join(sent_l))