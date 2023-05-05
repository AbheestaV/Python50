from twttr import shorten

def test_shorten():
    assert shorten("What's yOur name?5") == f"Wht's yr nm?5"
