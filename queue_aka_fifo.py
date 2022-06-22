class QueueError(BaseException):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if len(self.queue) > 0:
            val = self.queue[0]
            del self.queue[0]
            return val
        else:
            raise QueueError()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
