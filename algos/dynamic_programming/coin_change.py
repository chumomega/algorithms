def get_coin_change(amount: int, denominations: list) -> int:
    # dict has
        # key  = amount
        # value = dict()
            # key = tuple of denominations
            # value = total number of ways
    mem = dict()
    return get_change_helper(amount, denominations, 0, mem)

def get_change_helper(amount: int, denominations: list, pos: int, memory: dict) -> int:
    """Get amount of change. note this is recursive

    Args:
        amount: The first number.
        denominations: the denominations that you want change in (sorted reverse chronolological order)
        pos: index we are in the denominations list (to start giving change from)
        memory: previous calculations of change/amount left

    Returns:
        int: amount of change
    """
    coin = denominations[pos]

    # Base case
    if pos is len(denominations) - 1:
        # if 1 is last denomination, we don't need this. if it's not 1, we need to check divisibility
        remainder = amount % coin
        return 1 if remainder == 0 else 0
    
    denom_tuple = tuple(denominations[pos:])
    # only recalculate if not in memory
    if amount not in memory:
        memory[amount] = {}
    
    if denom_tuple not in memory[amount]:
        total = 0
        for new_amt in range(0, amount+1, coin):
            total += get_change_helper(
                amount=amount-new_amt,
                denominations=denominations,
                pos=pos+1,
                memory=memory
            )
        # update memory for use in other recursive trees if they're calculating the same thing
        if amount not in memory:
            memory[amount] = {}
        memory[amount][denom_tuple] = total
    
    return memory[amount][denom_tuple]


    
