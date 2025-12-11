from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    #You must take in *args a quantity of unknown number and make the Mean, Median,
    #Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
    #ask.
    if not args:
        print("ERROR")
        return
    data = sorted(args)
    n = len(data)
    mean = sum(data) / n
    median = data[n // 2] if n % 2 == 1 else (data[n // 2 - 1] + data[n // 2]) / 2
    # Simple quartile calculation: use the values at the 25% and 75% positions
    q1_idx = max(0, (n // 4) - (1 if n % 4 == 0 and n >= 4 else 0))
    q3_idx = min(n - 1, (3 * n) // 4)
    q1 = data[q1_idx]
    q3 = data[q3_idx]
    var = sum((x - mean) ** 2 for x in data) / n
    std = var ** 0.5
    # Accept requests either as kwarg keys or as kwarg values (e.g. toto="mean")
    for key, val in kwargs.items():
        requested = {str(key).lower(), str(val).lower()}
        if requested & {"mean"}:
            print(f"mean: {mean}")
        elif requested & {"median"}:
            print(f"median: {median}")
        elif requested & {"quartile"}:
            print(f"quartile: [{q1}, {q3}]")
        elif requested & {"std"}:
            print(f"std: {std}")
        elif requested & {"var"}:
            print(f"var: {var}")
