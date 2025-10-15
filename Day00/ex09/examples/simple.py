import pyflem


def main():
    pyflem.hello()
    print(pyflem.count_in_list([1, 2, 3, 3, 5], 3))
    print(pyflem.count_in_list([1, 2, 3, 3, 5], 4))
    pyflem.goodbye()


if __name__ == "__main__":
    main()
