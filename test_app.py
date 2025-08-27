from app import add

# This function is discovered by pytest
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# This makes python test_app.py also run the tests
if __name__ == "__main__":
    # Run the test function manually
    try:
        test_add()
        print("All tests passed!")
    except AssertionError as e:
        print("Test failed:", e)
        exit(1)  # exit with non-zero code so CI fails
