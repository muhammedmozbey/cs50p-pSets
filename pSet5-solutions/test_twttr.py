from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello, world") == "hll, wrld"