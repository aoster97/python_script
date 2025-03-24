def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # 按面额降序排序
    count = 0
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            result.append(coin)

    if amount > 0:
        return "无法找零"

    return count, result


# 示例
coins = [1, 5, 10, 25]
amount = 63
print(coin_change_greedy(coins, amount))  # 输出: (6, [25, 25, 10, 1, 1, 1])
