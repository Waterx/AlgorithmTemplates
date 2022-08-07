
class Solution:
    def maxValue(self, bag_size, weight, value):

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
        for i in range(1, cols):
            if weight[0] <= i: 
                dp[0][i] = value[0]

        # // 再处理「考虑其余物品」的情况
        for i in range(1, rows):
            for j in range(cols):

                # 不选该物品
                n = dp[i-1][j]

                # 选择该物品，前提「剩余容量」大于等于「物品体积」
                y = dp[i-1][j-weight[i]] + value[i] if j >= weight[i] else 0
                
                dp[i][j] = max(n, y)

        print(dp)
        return dp[-1][bag_size]


bag_size = 4
weight = [1, 3, 4]
value = [15, 20, 30]
c = Solution()
c.maxValue(bag_size, weight, value)
