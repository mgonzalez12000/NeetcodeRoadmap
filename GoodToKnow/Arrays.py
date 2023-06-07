# When working with a 2D array, you are able to append into a spiecifc list within a 2d array such as the following:

# Assume we have the following 2d array of strs
exampleArray = [["testOne", "testTwo", "testThree"], ["example1"]]

# We are able to append to the list in the first index so we can get [["testOne", "testTwo", "testThree", "APPENDED ELEMENT"]] by doing the following
exampleArray[0].append('APPENDED ELEMENT')
print(exampleArray)

