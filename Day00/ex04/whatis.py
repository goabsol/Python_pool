import sys

try:
    num = int(sys.argv[1])
    assert len(sys.argv) == 2, "more than one argument is provided"
except AssertionError as e:
    print(f"AssertionError: {e}")
    exit(1)
except ValueError:
    print("AssertionError: argument is not an integer")
    exit(1)
except IndexError:
    print("AssertionError: no argument is provided")
    exit(1)

if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
