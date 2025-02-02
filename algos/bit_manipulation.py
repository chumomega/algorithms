def add_wo_plus(n1: int, n2: int) -> int:
    if n2 == 0:
        return n1
    sum = n1 ^ n2
    carry = (n1 & n2) << 1
    return add_wo_plus(sum, carry)