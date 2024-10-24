from homefedsavingsbank import value

def main():
    test_value()

def test_value():
    assert value("hello there") == "$0"
    assert value("lo there") == "$100"
    assert value("Hey there") == "$20"
    assert value("name is David") == "$100"