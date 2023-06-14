# When working with a 2D array, you are able to append into a spiecifc list within a 2d array such as the following:

# Assume we have the following 2d array of strs
exampleArray = [["testOne", "testTwo", "testThree"], ["example1"]]

# We are able to append to the list in the first index so we can get [["testOne", "testTwo", "testThree", "APPENDED ELEMENT"]] by doing the following
# exampleArray[0].append("APPENDED ELEMENT")
# print(exampleArray)

# to iterate backwards on an array you can do the following for loop
exampleArray2 = [1, 2, 3, 4, 5]
for i in range(len(exampleArray2) - 1, -1, -1):
    print(exampleArray2[i])

print()

# iterate through the last two elements of a list
for i in range(len(exampleArray2) - 2, len(exampleArray2)):
    print(exampleArray2[i])
