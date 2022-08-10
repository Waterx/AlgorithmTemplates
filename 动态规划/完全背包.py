
# 记这个，和01背包的模板的差别只有第二层的遍历顺序
def maxValue_1d_press(bag_size, weight, value):

    dp = [0] * (bag_size + 1)

    for i in range(len(weight)):
        for j in range(weight[i], bag_weight + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    
    print(dp)

if __name__ == '__main__':
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    maxValue_1d_press(bag_weight, weight, value)
