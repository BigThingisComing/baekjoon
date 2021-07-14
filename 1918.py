infix_str = input()
op_stack = []
postfix = []

for i in infix_str:
  if ord(i) >= 65 and ord(i) <= 90:
    postfix.append(i)
  elif i == '(':
    op_stack.append(i)
  elif i == '+' or i == '-':
    while len(op_stack) != 0 and op_stack[len(op_stack)-1] != '(':
      postfix.append(op_stack.pop())
    op_stack.append(i)
  elif i == '*' or i == '/':
    while len(op_stack) != 0 and (op_stack[len(op_stack)-1] == '*' or op_stack[len(op_stack)-1] == '/'):
      postfix.append(op_stack.pop())
    op_stack.append(i)
  elif i == ')':
    while len(op_stack) != 0 and op_stack[len(op_stack)-1] != '(':
      postfix.append(op_stack.pop())
    op_stack.pop()

while len(op_stack) != 0:
  postfix.append(op_stack.pop())

print(''.join(postfix))