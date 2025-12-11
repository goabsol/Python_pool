from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates and prints requested statistics (mean, median, quartiles,
    variance, std) for given numeric arguments."""
    mean = median = q1 = q3 = var = std = 0
    if args:
        data = sorted(args)
        n = len(data)
        mean = sum(data) / n
        median = (data[n // 2] if n % 2 == 1
                  else (data[n // 2 - 1] + data[n // 2]) / 2)
        q1_idx = max(0, (n // 4) - (1 if n % 4 == 0 and n >= 4 else 0))
        q3_idx = min(n - 1, (3 * n) // 4)
        q1 = data[q1_idx]
        q3 = data[q3_idx]
        var = sum((x - mean) ** 2 for x in data) / n
        std = var ** 0.5
    for key, val in kwargs.items():
        if not args:
            print("ERROR")
            continue
        requested = {str(key).lower(), str(val).lower()}
        if requested & {"mean"}:
            print(f"mean: {mean}")
        elif requested & {"median"}:
            print(f"median: {median}")
        elif requested & {"quartile"}:
            print(f"quartile: [{float(q1)}, {float(q3)}]")
        elif requested & {"std"}:
            print(f"std: {std}")
        elif requested & {"var"}:
            print(f"var: {var}")
