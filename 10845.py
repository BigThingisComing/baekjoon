import sys
input = sys.stdin.readline

class Queue:
  def __init__(self):
    self.q = []
    self.len = 0
  
  def push(self, num):
    self.q.append(num)
    self.len += 1
  
  def pop(self):
    if self.len > 0:
      self.len -= 1
      tmp = self.q[0]
      self.q = self.q[1:]
      return tmp
    else:
      return -1
  
  def size(self):
    return self.len
  
  def empty(self):
    if self.len == 0:
      return 1
    else:
      return 0
  
  def front(self):
    if self.len == 0:
      return -1
    else:
      return self.q[0]

  def back(self):
    if self.len == 0:
      return -1
    else:
      return self.q[self.len-1]

com_num = int(input())

queue = Queue()

for i in range(com_num):
  Command = input().split()
  if Command[0] == 'push':
    queue.push(Command[1])
  elif Command[0] == 'pop':
    print(queue.pop())
  elif Command[0] == 'size':
    print(queue.size())
  elif Command[0] == 'empty':
    print(queue.empty())
  elif Command[0] == 'front':
    print(queue.front())
  elif Command[0] == 'back':
    print(queue.back())