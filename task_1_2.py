def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # ініціалізація таблиці мінімальної кількості монет
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # для суми 0 потрібні 0 монет

    # для відновлення шляху
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    # відновлюємо рішення
    result = {}
    i = amount
    while i > 0:
        coin = last_coin[i]
        result[coin] = result.get(coin, 0) + 1
        i -= coin

    return result

# Приклад використання
print("Dynamic:", find_min_coins(amount))  
# Очікувано: {50: 2, 10: 1, 2: 1, 1: 1} або аналогічно
