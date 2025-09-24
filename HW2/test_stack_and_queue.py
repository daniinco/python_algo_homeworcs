import pytest
from stack_and_queue import Stack, Queue

class TestStack:
    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.pop() == 2
        assert stack.pop() == 1
        try:
            stack.pop()
            assert False
        except IndexError:
            assert True


class TestQueue:
    def test_queue(self):
        queue = Queue()
        queue.push(1)
        queue.push(2)
        assert queue.pop() == 1
        assert queue.pop() == 2
        try:
            queue.pop()
            assert False
        except IndexError:
            assert True