from typing import List

"""给你一个整数数组 prices，其中prices[i] 表示某支股票第 i 天的价格。"""
"""在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。你也可以先购买，然后在 同一天 出售。返回你能获得的最大利润。"""
"""实现方法：将数组中所有的元素和前面一个相减，把大于0的结果相加"""


class Solution:
    def maxProfit(prices: List[int]) -> int:
        minus = []
        a = 0
        for i in range(0, len(prices) - 1):
            minus.append(prices[i + 1] - prices[i])
        for i in minus:
            if i > 0:
                a = a + i
        return a


print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
