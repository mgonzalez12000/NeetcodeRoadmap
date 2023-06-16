# Removing non alpha numerical:
example1 = 'Welcome, User_12!!'
new_str = ''.join(filter(str.isalnum, example1))
print(new_str) #WelcomeUser12
# Lower casing all uppercase chars:
new_str = new_str.lower()
print(new_str) # welcomeuser12