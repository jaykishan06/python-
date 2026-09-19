# Stack Implementation using List
# LIFO - Last In, First Out

stack = []


# Push Operation
def push(value):
    stack.append(value)
    print(value, "pushed into stack")


# Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print(stack.pop(), "popped from stack")


# Peek Operation
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])


# Display Operation
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack)


# Operations
push(10)
push(20)
push(30)

display()

peek()

pop()

display()

peek()
