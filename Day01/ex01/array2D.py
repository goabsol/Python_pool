def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("Expected a 2D list.")
    else:
        for member in family:
            if not isinstance(member, list):
                raise TypeError("Expected a 2D list.")
            if not all(isinstance(x, (int, float)) for x in member):
                raise TypeError("All elements in the 2D list must be numbers.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers.")
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(family[start:end])}, {len(family[0])})")
    return [member for member in family[start:end]]
