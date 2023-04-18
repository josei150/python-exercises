def find_fewest_coins(coins, target):
    fewest_coins = []

    if target in coins:
        fewest_coins.append(target)
        return fewest_coins

    coins = list(filter(lambda x: x < target, coins))
    coins.reverse()

    
    while sum(fewest_coins) != target:
        if coins[0] >= sum(fewest_coins) and sum(fewest_coins) != 0:
            coins.pop(0)
            continue

        if target % coins[0] == 0:
            for i in range(target // coins[0]):
                fewest_coins.append(coins[0])
            return fewest_coins
        


    return fewest_coins

    


if __name__ == "__main__":
    print(find_fewest_coins([1, 5, 10, 25], 1)) #[1]
    print(find_fewest_coins([1, 5, 10, 21, 25], 63)) #[21, 21, 21]

    #print(find_fewest_coins([1, 5, 10, 25, 100], 15)) #[5, 10]