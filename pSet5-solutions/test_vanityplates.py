from vanityplates import is_valid


def main ():
    test_valid()

def test_valid():
    assert is_valid("CS50") == "Valid"
    assert is_valid("CS05") == "Invalid"
    assert is_valid("CS50P") == "Invalid"
    assert is_valid("PI3.14") == "Invalid"
    assert is_valid("H") == "Invalid"
    assert is_valid("OUTATIME") == "Invalid"