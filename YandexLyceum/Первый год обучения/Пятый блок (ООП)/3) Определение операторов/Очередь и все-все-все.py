class Queue:
    def __init__(self, *args):
        self.queue = [i for i in args]

    def append(self, *values):
        for num in values:
            self.queue.append(num)

    def copy(self):
        res = Queue()
        res.queue += self.queue
        return res

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return

    def extend(self, other):
        self.queue += other.queue

    def next(self):
        new = self.copy()
        new.queue = new.queue[1:]
        return new

    def __add__(self, other):
        new = self.copy()
        new.queue += other.queue
        return new

    def __iadd__(self, other):
        self.queue += other.queue
        return self

    def __eq__(self, other):
        return self.queue == other

    def __rshift__(self, n):
        if len(self.queue) > n:
            new = Queue()
            new.queue += self.queue[n:]
            return new
        return Queue()

    def __str__(self):
        return '[' + ' -> '.join(map(str, self.queue)) + ']'

    def __next__(q):
        new = q.copy()
        new.queue = new.queue[1:]
        return new


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)