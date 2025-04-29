from main import add

def test_add():
    try:
        assert add(2, 3) == 5
        print("Test 1 Passed: add(2, 3) == 5")
    except AssertionError:
        print("Test 1 Failed: add(2, 3) != 5")

    try:
        assert add(0, 0) == 0
        print("Test 2 Passed: add(0, 0) == 0")
    except AssertionError:
        print("Test 2 Failed: add(0, 0) != 0")

    try:
        assert add(-1, 1) == 0
        print("Test 3 Passed: add(-1, 1) == 0")
    except AssertionError:
        print("Test 3 Failed: add(-1, 1) != 0")

# Run the test function
test_add()