'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []

    def push(self, val: int) -> None:
        curmin = self.getMin()
        if curmin == None or val < curmin:
            curmin = val
        self.Stack.append((val,curmin))

    def pop(self) -> None:
        self.Stack.pop()

    def top(self) -> int:
        if len(self.Stack) == 0:
            return None
        else:
            return self.Stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.Stack) == 0:
            return None
        else:
            return self.Stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
