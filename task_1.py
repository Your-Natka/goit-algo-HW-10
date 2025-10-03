from collections import defaultdict

coins = [50, 25, 10, 5, 2, 1]

# -------------------------
# Жадібний алгоритм
# -------------------------
def find_coins_greedy(amount):
    result = defaultdict(int)
    remaining = amount
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    return dict(result)

# -------------------------
# Динамічне програмування
# -------------------------
def find_min_coins(amount):
    # Ініціалізація масиву dp: dp[i] = мінімальна кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 монет для суми 0

    # Масив для відстеження останньої використаної монети
    last_coin = [-1] * (amount + 1)

    # Заповнення dp
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення складу монет
    result = defaultdict(int)
    current = amount
    while current > 0:
        coin = last_coin[current]
        if coin == -1:  # Немає рішення
            return {}
        result[coin] += 1
        current -= coin

    return dict(result)

# -------------------------
# Перевірка роботи
# -------------------------
amount = 113

greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

print(f"Сума: {amount}")
print("Жадібний алгоритм:", greedy_result, " | Кількість монет:", sum(greedy_result.values()))
print("Динамічне програмування:", dp_result, " | Кількість монет:", sum(dp_result.values()))
