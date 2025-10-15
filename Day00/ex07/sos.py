import sys


def main():
    try:
        assert len(sys.argv) == 2 and sys.argv[1].isalnum(), \
             "the arguments are bad"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    except Exception as e:
        print("Exception:", e)
        exit(1)
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/ '
    }
    words = sys.argv[1].upper()
    print(" ".join([NESTED_MORSE.get(x, x) for x in words]))


if __name__ == "__main__":
    main()
