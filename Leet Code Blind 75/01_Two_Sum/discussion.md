## General solution
The first solution that come in to mind is to do a brute force two nested loop solution. outer loop will go from left to right and the inner loop also go from left to right for each iteration of outer loop unless we find the solution pair.

```python
# Brute force solution
def twoSum(nums, target):
    for opening_index in range(len(nums)-1):
        for closing_index in range(opening_index + 1, len(nums)):
            if nums[opening_index] + nums[closing_index] == target:
                return [opening_index, closing_index]
```
**Time complexity**: *O(n<sup>2</sup>)*

## Optimized approach 1
Sorting gives a additional control when working on finding/searching items in an array or list. Not always but there is a possibility. 
So if we sort the list, we know the left most item is the smallest and the right most is the largest.
if we add the `left_most` with the `right_most` here the possible outcomes:
- `left_most` + `right_most` > `target` | We need to consider previous `right_most`
- `left_most` + `right_most` < `target` | We need to consider next `left_most`
- `left_most` + `right_most` = `target` | We have the numbers.

Since we have the numbers, we now will do a linear iteration to get their indexes.

```python
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
```

**Time complexity**: *O(n**log**n)* + *O(n)* => *O(n**log**n)*

## Optimized approach 2 (Hash Map)
Hash map have the feature of low `O(1)` insertion time and search time. Since we can put it as an `equation` => `item1` + `item2` = `target` we can try with Hash map to find a solution. We will iterate through the list ine time, for each item we will calculate the `compliment` first. Then we need to search for the `compliment` in the Hash map, if the hash map have the complement we have out pair. If not, we will add the item in the hash map with index as a value.

```python
def twoSumHashMap(nums, target):
    hash_map = {}
    for index in range(len(nums)):
        compliment = target - nums[index]
        if compliment in hash_map:
            return [hash_map[compliment], index]
        hash_map[nums[index]] = index
```

**Time complexity**: O(n)
**Space complexity**: O(n)