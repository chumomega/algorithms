def is_unique(random_str: str) -> bool:
    # ascii or unicode? assume ascii
        # if ascii, we can use array w fixed size
        # if unicode, we can just use a hashmap bc the size is vv large
    # 256 characters in ASCII
    char_counter = [0] * 256
    for char in random_str:
        # ord gets the numeric value of a character (for ascii)
        num_value_of_str = ord(char)
        if char_counter[num_value_of_str] == 1:
            return False
        else:
            char_counter[num_value_of_str] = 1
    return True

    