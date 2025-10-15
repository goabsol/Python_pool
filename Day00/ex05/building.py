import sys


def is_punctuation(c):
    '''
    This function is used to check if a character is a punctuation mark.
    '''
    return c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def main():
    '''
    This module is used to count the number of upper letters, lower letters,
    punctuation marks, spaces, and digits in a given string.
    '''
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        assert len(sys.argv) == 2, "please provide one string argument"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    except Exception as e:
        print("Exception:", e)
        exit(1)
    building = sys.argv[1]
    print(f"The text contains {len(building)} characters:")
    print(f"{len([c for c in building if c.isupper()])} upper letters")
    print(f"{len([c for c in building if c.islower()])} lower letters")
    print(f"{len([c for c in building if is_punctuation(c)])} \
punctuation marks")
    print(f"{len([c for c in building if c.isspace()])} space")
    print(f"{len([c for c in building if c.isdigit()])} digits")


if __name__ == "__main__":
    main()
