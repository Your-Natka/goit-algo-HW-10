def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    remaining = amount
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    return result

# Приклад використання
amount = 113
print("Greedy:", find_coins_greedy(amount))  
# Очікувано: {50: 2, 10: 1, 2: 1, 1: 1}