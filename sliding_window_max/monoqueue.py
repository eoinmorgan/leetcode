class Monoqueue:
    """
    Implements a queue with the monotonic decreasing invariant. Nameley:
        
        for all i,k i < k: queue[i] >= queue[k]

    This invariant is enforced by truncating the tail of the queue when inserting a new element. For example, If the new element is strictly greater than all existing elements, all other elements will be truncated before insertion and the new element will be the only element in the queue.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Adds a new element to the queue, truncating the tail of the queue to maintain the monotonic invariant.
        """
        while len(self.items) > 0 and self.items[-1] < item:
            self.items.pop(-1)
        self.items.append(item)

    def front(self):
        """
        Allows "peeking" at the maximum value in the queue.
        """
        return self.items[0]

    def pop(self, item):
        """
        Removes the maximum value in the queue if it is equal to `item`
        """
        if item == self.items[0]:
            self.items.pop(0)
