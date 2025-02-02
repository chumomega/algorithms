from algos.bit_manipulation import add_wo_plus, subtract_wo_minus

def test_add_wo_sum():
    num1 = 241
    num2 = 79

    expected_sum = 320
    actual_sum = add_wo_plus(num1, num2)

    assert expected_sum == actual_sum

    num1 = -241
    num2 = 79

    expected_sum = -162
    actual_sum = add_wo_plus(num1, num2)

    assert expected_sum == actual_sum

    num1 = 0
    num2 = 79

    expected_sum = 79
    actual_sum = add_wo_plus(num1, num2)

    assert expected_sum == actual_sum

    num1 = -13
    num2 = 0

    expected_sum = -13
    actual_sum = add_wo_plus(num1, num2)

    assert expected_sum == actual_sum
    

def test_subtract_wo_minus():
    num1 = 241
    num2 = 79

    expected_diff = 162
    actual_sum = subtract_wo_minus(num1, num2)

    assert expected_diff == actual_sum


