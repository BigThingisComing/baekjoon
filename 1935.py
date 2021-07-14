def Cal_Postfix(num, postfix):
  str_to_num = []
  stack = []
  result = 0

  for _ in range(num):
    str_to_num.append(int(input()))
  
  for i in postfix:
    if ord(i) >= 65 and ord(i) <= 90:
      stack.append(str_to_num[ord(i)-65])
    elif i == '*':
      tmp1 = stack.pop()
      tmp2 = stack.pop()
      stack.append(tmp1 * tmp2)
    elif i == '/':
      tmp1 = stack.pop()
      tmp2 = stack.pop()
      stack.append(tmp2 / tmp1)
    elif i == '+':
      tmp1 = stack.pop()
      tmp2 = stack.pop()
      stack.append(tmp1 + tmp2)
    elif i == '-':
      tmp1 = stack.pop()
      tmp2 = stack.pop()
      stack.append(tmp2 - tmp1)
  
  return stack.pop()

append_num = int(input())
pf_str = input()

print("{:.2f}".format(Cal_Postfix(append_num, pf_str)))