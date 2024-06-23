class MyQueue:
    """
    This class implements a queue data structure with a limited capacity.
    """
    def __init__(self, capacity):
        """
        Initializes the queue with a specified capacity.

        Args:
        capacity: The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0
    
    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
        True if the queue is full, False otherwise.
        """
        return len(self.queue) == self.capacity
    
    def enqueue(self, value):
        """
        Adds a new element to the back of the queue.

        Raises:
        Exception: If the queue is full.
        """
        if self.is_full():
            print('Queue is full')
        return self.queue.append(value)
    
    def dequeue(self):
        """
        Removes and returns the first element from the queue.

        Raises:
        Exception: If the queue is empty.
        """
        if self.is_empty():
            print('Queue is empty')
        return self.queue.pop(0)
    
    def front(self):
        """
        Returns the first element of the queue without removing it.

        Raises:
        Exception: If the queue is empty.
        """
        if self.is_empty():
            print('Queue is empty')
        return self.queue[0]