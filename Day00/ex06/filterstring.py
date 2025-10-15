import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3 and not sys.argv[1].isnumeric() \
            and sys.argv[2].isnumeric(), "the arguments are bad"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    except Exception as e:
        print("Exception:", e)
        exit(1)
    words = sys.argv[1].split()
    length = int(sys.argv[2])
    print(list(ft_filter(lambda x: len(x) > length, words)))
    print(ft_filter(None, words))


if __name__ == "__main__":
    main()
