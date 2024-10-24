from fuelgauge import fraction

def main():
    test_fraction()

def test_fraction():
    assert fraction("3/4") == "75%"
    assert fraction("1/4") == "25%"
    assert fraction("4/4") == "Full"
    assert fraction("0/4") == "Empty"