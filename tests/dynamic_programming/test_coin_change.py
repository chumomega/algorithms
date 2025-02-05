from algos.dynamic_programming.coin_change import get_coin_change

def test_get_coin_change():
    amount = 26
    denominations = [25, 10, 5, 1]

    num_ways_to_make_change = get_coin_change(amount, denominations)
    assert num_ways_to_make_change == 13
    # 1q 1p
    # 2d 1n 1p
    # 2d 6p
    # 1d 3n 1p
    # 1d 2n 6p
    # 1d 1n 11p
    # 1d 16p
    # 5n 1p
    # 4n 6p
    # 3n 11p
    # 2n 16p
    # 1n 21p
    # 26p