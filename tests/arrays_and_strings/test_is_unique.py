
from algos.arrays_and_strings.is_unique import is_unique
def test_is_unique():
    rand_str1 = "abcdefga"
    rand_str2 = ""
    rand_str3 = "abc123abc"
    rand_str4 = "uniqeStrg"

    assert is_unique(random_str=rand_str1) == False
    assert is_unique(random_str=rand_str3) == False
    assert is_unique(random_str=rand_str4) == True
    assert is_unique(random_str=rand_str2) == True
    
