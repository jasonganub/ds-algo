class Stack:
  def __init__(self):
    self.stack = []

  def length(self):
    return len(self.stack)

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def is_empty(self):
    return self.stack == []

s = Stack()
print("length {}".format(s.length()))
s.push(1)
s.push(2)
print("pushed item 1 and 2")
print("length {}".format(s.length()))
print("peek {}".format(s.peek()))
print("is empty? {}".format(s.is_empty()))
print("popped {}".format(s.pop()))
print("popped {}".format(s.pop()))
print(s.length())
print("is empty? {}".format(s.is_empty()))