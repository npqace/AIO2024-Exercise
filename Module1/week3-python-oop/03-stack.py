class MyStack:
    """
    This class implements a stack data structure with a limited capacity.
    """

    def __init__(self, capacity):
        """
        Initializes the stack with a specified capacity.

        Args:
        capacity: The maximum number of elements the stack can hold.
        """
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def is_full(self):
        """
        Checks if the stack is full.

        Returns:
        True if the stack is full, False otherwise.
        """
        return len(self.stack) == self.capacity

    def pop(self):
        """
        Removes and returns the top element from the stack.

        Raises:
        Exception: If the stack is empty.
        """
        if self.is_empty():
            print('Stack is empty')
        return self.stack.pop()

    def push(self, value):
        """
        Adds a new element to the top of the stack.

        Raises:
        Exception: If the stack is full.
        """
        if self.is_full():
            print('Stack is full')
        return self.stack.append(value)

    def top(self):
        """
        Returns the top element of the stack without removing it.

        Raises:
        Exception: If the stack is empty.
        """
        if self.is_empty():
            print('Stack is empty')
        return self.stack[-1]
