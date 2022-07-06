def twoSum(nums, target):
    hashmap = {}
    for k, num in enumerate(nums):
        hashmap[num] = k
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]

# enumerate(sequence, [start=0]),会返回（下标，列表中的值）
# for 中的i，num正好对应了两个参数 从前面往后扫过去就可以找到和当前不一样位置的解
