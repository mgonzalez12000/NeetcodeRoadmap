def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.

    0 is red
    1 is white
    2 is blue
    """
    red = 0
    white = 0
    blue = len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


t1 = [2, 0, 2, 1, 1, 0]
t2 = [2, 0, 1]


print(sortColors(t1))
print(sortColors(t2))
