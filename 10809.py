alcount = [-1 for i in range(26)]

string = input()

for i in range(len(string)):
  if alcount[ord(string[i])-97] == -1:
    alcount[ord(string[i])-97] = i

for i in range(len(alcount)):
  alcount[i] = str(alcount[i])

print(' '.join(alcount))