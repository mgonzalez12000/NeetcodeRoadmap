# Removing non alpha numerical:
example1 = 'Welcome, User_12!!'
new_str = ''.join(filter(str.isalnum, example1))
print(new_str) #WelcomeUser12
# Lower casing all uppercase chars:
new_str = new_str.lower()
print(new_str) # 

# finding a min and/or max for a solution
# you can use the min() or max() function to check for a min or max value (typcailly in a loop) where both functions take in two args. Current value and new value