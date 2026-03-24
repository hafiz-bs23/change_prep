# Brute force solution
def twoSum(nums, target):
    for opening_index in range(len(nums)-1):
        for closing_index in range(opening_index + 1, len(nums)):
            if nums[opening_index] + nums[closing_index] == target:
                return [opening_index, closing_index]
            
# Two pointer solution
def twoSumTwoPointer(nums, target):
    sorted_nums = sorted(nums)
    opening_index = 0
    closing_index = len(nums) - 1
    while opening_index < closing_index:
        left_most = sorted_nums[opening_index]
        right_most = sorted_nums[closing_index]
        two_sum = left_most + right_most
        if two_sum == target:
            return [nums.index(left_most), nums.index(right_most)]
        elif two_sum < target:
            opening_index += 1
        else:
            closing_index -= 1
            
# Hash map solution
def twoSumHashMap(nums, target):
    hash_map = {}
    for index in range(len(nums)):
        compliment = target - nums[index]
        if compliment in hash_map:
            return [hash_map[compliment], index]
        hash_map[nums[index]] = index
            
if __name__ == "__main__":
    nums_inputs = [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    target_inputs = [18, 6, 6, 11]
    # Check brute force solution
    for nums, targets in zip(nums_inputs, target_inputs):
        print(f"Brute force solution: {twoSum(nums, targets)}")
        print(f"Two pointer solution: {twoSumTwoPointer(nums, targets)}")
        print(f"Hash map solution: {twoSumHashMap(nums, targets)}")
        