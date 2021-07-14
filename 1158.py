n,k = map(int, input().split())
people = [i for i in range(1, n+1)]
queue = []

del_people = 0

for i in range(n):
  del_people += k-1
  if del_people >= len(people):
    del_people = del_people%len(people)
  
  queue.append(str(people.pop(del_people)))

print('<', ', '.join(queue)[:], '>', sep='')