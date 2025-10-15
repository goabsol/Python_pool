def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists.")
    if (not all(isinstance(x, (int, float)) for x in height)
            or not all(isinstance(x, (int, float)) for x in weight)):
        raise TypeError("All elements in height list must be numbers.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    l: list[int | float] = []
    for i in range(len(height)):
        bmi = weight[i] / (height[i] ** 2)
        l.append(bmi)
    return l


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("All elements in BMI list must be numbers.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    return [x > limit for x in bmi]
