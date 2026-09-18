class QueueFromStacks:
    def __init__(self):
        self.in_stack = []   # for enqueue
        self.out_stack = []  # for dequeue

    def enqueue(self, x) -> None:
        """Always O(1)"""
        self.in_stack.append(x)

    def dequeue(self):
        """Amortized O(1). Raises error if queue is empty."""
        if not self.out_stack:
           
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("dequeue from empty queue")

        return self.out_stack.pop()


# ==================== Tests ====================
if __name__ == "__main__":
    q = QueueFromStacks()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())  
    print(q.dequeue())  

    q.enqueue(4)
    print(q.dequeue()) 
    print(q.dequeue())  

  
    try:
        q.dequeue()
    except IndexError as e:
        print("Error correctly raised:", e)
