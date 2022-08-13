
class Solution:

    # 记这个，推理过程看宫水三叶以及下面的2d完整版和滚动数组版
    def maxValue_1d_press(self, bag_size, weight, value):

        dp = [0] * (bag_size + 1)

        for i in range(len(weight)):
            for j in range(bag_size, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
                # 求组合类用的是这个，初始化 dp[0] = 1，理论上也很好解释，装满容量为0的背包，有1种方法，就是装0件物品。
                # dp[j] += dp[j - nums[i]] 

        print(dp)
        return dp[bag_size]

    def maxValue_2d(self, bag_size, weight, value):

        #    容量  0   1   2   3   ……  j
        #        ______________________
        # 物品 0 |  
        # 物品 1 |  
        # 物品 2 |  
        # 物品 ……|  
        # 物品 i |  

        rows, cols = len(weight), bag_size + 1
        dp = [[0] * cols for _ in range(rows)]

        # 先处理「考虑第一件物品」的情况
        for i in range(cols):
            if weight[0] <= i: dp[0][i] = value[0]

        # 再处理「考虑其余物品」的情况
        for i in range(1, rows):
            for j in range(cols):

                # 不选该物品
                n = dp[i-1][j]

                # 选择该物品，前提「剩余容量」大于等于「物品体积」
                y = dp[i-1][j-weight[i]] + value[i] if j >= weight[i] else 0
                
                dp[i][j] = max(n, y)

        print(dp)
        return dp[-1][bag_size]


    def maxValue_rotate(self, bag_size, weight, value):

        rows, cols = 2, bag_size + 1
        dp = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            if weight[0] <= i: dp[0][i] = value[0]

        for i in range(1, rows):
            for j in range(cols):

                n = dp[(i-1)&1][j]
                y = dp[(i-1)&1][j-weight[i]] + value[i] if j >= weight[i] else 0
                
                dp[i&1][j] = max(n, y)

        n = len(weight)
        print(dp, dp[n&1][bag_size])
        return dp[n&1][bag_size]


bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]
c = Solution()
c.maxValue_2d(bag_size, weight, value)
c.maxValue_rotate(bag_size, weight, value)
c.maxValue_1d_press(bag_size, weight, value)
