"""
Definition of stack:
stack is a linear data structure, but insertions and deletion are only allowed at the end of stack 
AKA top of the stack. This is known as a LIFO stack. Last In, First Out.
Real life examples: Think of a STACK of books. When you are trying to get a book from a stack,
the only way you can really get the book is by removing a book from the TOP of the stack, or else,
the entire book stack can tumble and fall down. 

Primary stack operations:
push(): Inserts data onto the stack to the "top" element of the stack
pop(): Deletes the last inserted element from the stack AKA deletes the "top" element of the stack
top(): Returns the top element of the stack
size(): Returns the size of the stack
isEmpty(): Returns a boolean value if the stack is empty or not. A stack is empty if the stack
           does not have elements within it and/or the length/size of the stack is 0.

Implement stack in python:
A stack in python is simply a list [] data structure.
.push() = .append() in python
.pop() = .pop() in python DO NOT GET IT CONFUSED WITH .remove() as remove takes in a specific element
removes it from the list. 
"""
