"""
This python script is intended to save helpful tips for the
hashmap/dictionary data structure.
"""
# When working with a dictioanry, you are able to get the value of a key using .get
# Assume we have the following populated dictionary
dict = {"item1" : 1, "item2" : 2, "item3" : 3}

# to get the values of a specified key, you can do the following
print('Printing the first keys value')
print(dict.get('item1'))

# if you want to add all the keys in your dict to a list, you can do:
lst = []
for key in dict.keys():
    lst.append(key)
print('\nlist of keys in dictionary')
print(lst)

# if you want to add all the values in your dict to a list, you can do:
lst_values = []
for key in dict.keys():
    lst_values.append(dict[key])
print('\nlist of values in dictionary')
print(lst_values)

# if you want to sort your keys you can do the following
# assume we have a brand new dictionary such as
dict2 = {"c":1, "a": 4, "o": 3, "b": 0}
# printing the original dictionary without sorting
print("\nprinting the original dictionary")
print(dict2)
# now we are going to sort the dictionary based on the key
sorted_dict = sorted(dict2)
print('printing the newly sorted dictionary based on keys')
print(sorted_dict)

# what if we want to sort the dictionaty based on value? We can do the following
sorted_values = sorted(dict2, key=dict2.get)
print('printing the newly sorted keys based on values')
print(sorted_values)