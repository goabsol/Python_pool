def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    elif object != object and isinstance(object, float):
        print(f"Cheese: nan {type(object)}")
        return 0
    elif not object and isinstance(object, bool):
        print(f"Fake: False {type(object)}")
        return 0
    elif not object and isinstance(object, int):
        print(f"Zero: 0 {type(object)}")
        return 0
    elif not object and isinstance(object, str):
        print(f"Empty: {type(object)}")
        return 0
    print("Type not Found")
    return 1
