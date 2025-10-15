def count_in_list(lst: list, value) -> int:
    '''
    Count the number of occurrences of a value in a list.
    '''
    try:
        return lst.count(value)
    except AttributeError as e:
        print(f"Error: {e}")
        return 0
