import numpy as np


def add_wo_plus(n1: int, n2: int) -> int:
    if n2 == 0:
        return n1
    sum = n1 ^ n2  # XOR makes each bit 0 if same and 1 if different
    carry = (
        n1 & n2
    ) << 1  # AND makes each bit 0 unless both 1. then we shift to left bc carry
    return add_wo_plus(sum, carry)


def subtract_wo_minus(n1: int, n2: int) -> int:
    # i use numpy here bc python by default has no boundary on integers
    # so when you get 2s complement, it can be infinite num of bits causing timeouts in loop or recursion
    # numpy forces the numbers to be at most 32 bits
    twos_complement = (
        ~np.int32(n2) + 1
    )  # 2s complement is how computers represent negative numbers
    return int(add_wo_plus(np.int32(n1), twos_complement))
