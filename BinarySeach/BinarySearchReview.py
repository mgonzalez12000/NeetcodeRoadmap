"""
Binary search notes: Before getting into the binary seach algorithm, 
I suggest you heavily review pointers and feel comfortable with pointers.

The easiest way to grasp the concept of the binary search algorithm 
is to think of a SORTED cabinet trying to find a portfolio's last name.
Upon your first look, if you land above a letter before the given name, 
you ignore everything on the left and shift over to the rest, and repeat
this process until you find your portfolio.

The same concept applies here:
- have a left pointer
- have a right pointer
- have a middle pointer
- the middle pointer will be your target checker ( what you are looking for)

Best case time complexity for binary search algorithm is o(1)
where worst case can be o(log n)
"""