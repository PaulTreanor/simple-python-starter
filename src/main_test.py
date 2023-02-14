from main import add
def test_success():
    assert add(1, 2) == 3
def test_failure():
    assert add(1, 2) == 4