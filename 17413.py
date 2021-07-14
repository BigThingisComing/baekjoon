import sys
input = sys.stdin.readline

string = input().rstrip()

tmp = ''
result = ''

tag_tf = False

for chari in string:
  if tag_tf == False:
    if chari == '<':
      tag_tf = True
      tmp = tmp + chari
    elif chari == ' ':
      tmp = tmp + chari
      result = result + tmp
      tmp = ''
    else:
      tmp = chari + tmp

  else:
    tmp = tmp + chari
    if chari == '>':
      tag_tf = False
      result = result + tmp
      tmp = ''

result = result + tmp

print(result)