tc = int(input())

for i in range(tc):
  q = input()
  score = 0

  tmp = 0

  for j in range(len(q)):
    if q[j] == 'O':
      tmp += 1
      score += tmp
    else:
      tmp = 0
  
  print(score)