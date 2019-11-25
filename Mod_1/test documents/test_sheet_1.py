def sum67(nums):
    new_list = []
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            print(i)
            i = nums.index(7) + 1
        else :
            new_list.append(nums[i])
            print(i)
            i += 1
    return sum(new_list)

test_list = [5, 6, 1000, 400, 7, 10, 10]

print(sum67(test_list))
