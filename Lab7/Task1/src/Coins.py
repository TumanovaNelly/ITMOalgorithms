from typing import List, Dict, Union

from utils import read, write


def count_coins_no_borders(price: int, coins: List[int]):
    count_list: List[Union[float('inf'), int]] = [float('inf')] * (price + 1)
    count_list[0] = 0

    for i in range(len(count_list)):
        for coin in coins:
            if i - coin < 0: continue
            count_list[i] = min(count_list[i], count_list[i - coin] + 1)

    return count_list[price] if count_list[price] != float('inf') else None


def count_coins_with_borders_optimized(price: int, coins: Dict[int, int]):
    count_list = [float('inf')] * (price + 1)
    count_list[0] = 0

    for coin, count in coins.items():
        current_count = 1
        while current_count <= count:
            for x in range(price, coin * current_count - 1, -1):
                count_list[x] = min(count_list[x], count_list[x - coin * current_count] + current_count)
            count -= current_count
            current_count *= 2
        if count > 0:
            for x in range(price, coin * count - 1, -1):
                count_list[x] = min(count_list[x], count_list[x - coin * count] + count)

    return count_list[price] if count_list[price] != float('inf') else -1


def main():
    (price,), coins = read()
    write(count_coins_no_borders(price, coins))


if __name__ == "__main__":
    main()
