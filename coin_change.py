from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    coins.sort(reverse=True)
    print(coins)
    if amount == 0:
        return 0
    if amount < coins[-1]:
        return -1
    p = coins[0]
    candidate = p
    count = 0
    sum = 0
    for x in coins:
        print("x is", x)
        candidate = x
        while (sum + candidate <= amount):
            print("candidate is",candidate)
            print("sum is", sum)
            print("count is", count)
            count += 1
            sum = sum + candidate
            print("sum her is",sum)
        if sum == amount:
            return count
    return -1
coinChange([186,419,83,408], 6249)
