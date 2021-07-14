import sys

while True:
  string = sys.stdin.readline().rstrip('\n')
  uc, lc, sp, num = 0, 0, 0, 0

  if not string:
    break
  for i in string:
    if i.isupper():
      uc += 1
    elif i.islower():
      lc += 1
    elif i.isdigit():
      num += 1
    elif i.isspace():
      sp += 1

  sys.stdout.write("{} {} {} {}\n".format(lc, uc, num, sp))