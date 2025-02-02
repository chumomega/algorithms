def add_wo_plus(n1: int, n2: int) -> int:
    sol = 0
    carry = 0
    
    while n1 != 0 or n2 != 0 or carry != 0:
        bit1 = 1 if n1 & 1 == 1 else 0
        bit2 = 1 if n1 & 1 == 1 else 0
        n1 = logical_right_shift(n1, 1)
        n2 = logical_right_shift(n2, 1)

        new_carry = bit1 & bit2
        new_bit = 0 if new_carry == 1 else (bit1 | bit2)
        if (carry & new_bit) == 1:
            new_carry = 1
        else:
            new_bit = carry

        sol <<= 1
        sol = sol | new_bit
    reversed_bin = bin(sol)[:1:-1]
    return int(reversed_bin, 2)

def logical_right_shift(n, shift, bit_width=32):
    mask = (1 << bit_width) - 1  # For bit_width=32, mask is 0xFFFFFFFF
    n &= mask  # Interpret n as a 32-bit unsigned integer
    return n >> shift

if __name__ == '__main__':
    print("Start tests")

    num1 = 241
    num2 = 79

    expected_sum = 320
    actual_sum = add_wo_plus(num1, num2)
    print(f"Actual sum: {actual_sum}")

    try:
        assert 5 == 5
        assert expected_sum == actual_sum
    except AssertionError as e:
        print(e)

    print("End of tests")
    