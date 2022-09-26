'''
Lab 3 - Code 1 - Stack ADT.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

Write a python program using classes to implement a stack with the following menu options,
1) Push
2) Pop
3) Peek
4) Display
5) Exit

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("Top of Stack ->")
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):

        if self.isEmpty():
            print("Error!!! Peeking from an empty stack")
        else:
            return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Error!!! Popping from an empty stack")
        else:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return remove.value

    def display(self):
        if self.isEmpty():
                print("Error!!! Empty Stack")
        else :
                tnode = self.head
                while(tnode is not None):
                        print(tnode.value,'|', end=" ")
                        tnode = tnode.next

stack = Stack()

while True:

        print("\nMenu Driven Program for Queue : \n")
        print("   1. Push ")
        print("   2. Pop ")
        print("   3. Peek ")
        print("   4. Display ")
        print("   5. Exit ")
        choice = int(input("\nEnter the choice : "))

        if choice == 1:
            value = input("\nEnter the value to be pushed: ")
            stack.push(value)

        elif choice == 2:
            popped = stack.pop()
            if stack.isEmpty():
            	print(end=" ")
            else:
            	print('Popped element: ', popped)
        elif choice == 3:
            peeked = stack.peek()
            if stack.isEmpty():
                print(end=" ")
            else:
                print('The top element is : ', peeked)
        elif choice == 4:
            if stack.isEmpty():
                print('Stack is empty.')
            else:
                print('The elements present in the stack are : ')
                stack.display()
            print()
        elif choice == 5:
                break
                
