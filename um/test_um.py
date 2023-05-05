from um import count

def test_um():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um, um... yummy") == 2
    assert count("umum") == 0
    assert count("Um") == 1
    assert count ("Um, thanks for the album") == 1