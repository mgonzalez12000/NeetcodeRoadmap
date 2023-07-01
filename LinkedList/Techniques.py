'''
The runner technique: The runner technique means that you iterate through the linkedlist with two pointers simultaenously,
with one ahead of the other. AKA both pointer go through the chain at different speeds at the same time.
When iterating through the chain of the linkedlist, you can implement two pointers A and B
Arbitrarily pointer A can iterate "one" object, while pointer B can iterate over "two" objects while iterating through the LL
chain. 

The fast node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through
'''