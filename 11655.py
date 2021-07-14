import sys
string = list(sys.stdin.readline().rstrip('\n'))

for i in range(len(string)):
  if ord(string[i]) >= 65 and ord(string[i]) <= 90:
    string[i] = chr((ord(string[i]) - 65 + 13) % 26 + 65)
  elif ord(string[i]) >= 97 and ord(string[i]) <= 122:
    string[i] = chr((ord(string[i]) - 97 + 13) % 26 + 97)

print(''.join(string))