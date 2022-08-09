'''
Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

'''



class MyStack:

    def __init__(self):
        self.que = deque()
        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]
        

    def empty(self) -> bool:
        return not self.que
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()





#method 1
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.q1)
      


#method 2:(not recommended)
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.q1)
      

