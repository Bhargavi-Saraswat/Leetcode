class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 1:
            return self.stack.pop()

        top = self.stack.pop()

        result = self.pop()

        self.stack.append(top)

        return result

    def peek(self) -> int:
        if len(self.stack) == 1:
            return self.stack[-1]

        top = self.stack.pop()

        result = self.peek()

        self.stack.append(top)

        return result

    def empty(self) -> bool:
        return len(self.stack) == 0