alcount = [0 for i in range(26)]

string = input()

for i in string:
  alcount[ord(i)-97] += 1

for i in range(len(alcount)):
  alcount[i] = str(alcount[i])

print(' '.join(alcount))