import pytest
import reverseList

# Here are a few basic example they give for pyetst in the documentation.
# Run code with either pytest <filename> or python -m pytest <filename>

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4

# This is the way to test if some code raises an exception
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# You can group tests together under one class
class TestClass():
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert x == 'hello'

# Now here are your own test statements
class TestReverseList():
    def test_reverselist(self):
        assert(reverseList.reverse_list([1, 2, 3]) == [3, 2, 1])

    def test_reverselist2(self):
        assert(reverseList.reverse_list([]) == [])

    def test_reverselist3(self):
        assert(reverseList.reverse_list(["hello", "world"]) == ["world", "hello"])






