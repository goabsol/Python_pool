class calculator:
    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Calculate the dot product of two vectors v1 and v2."""
        dot_product = 0.0
        for i in v1:
            dot_product += i * v2[v1.index(i)]
        print(f"Dot product: {int(dot_product)}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Add two vectors v1 and v2."""
        result = []
        for i in v1:
            result.append(i + v2[v1.index(i)])
        print(f"Add vector: {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Subtract vector v2 from vector v1."""
        result = []
        for i in v1:
            result.append(i - v2[v1.index(i)])
        print(f"Sous vector: {[f'{val:.1f}' for val in result]}")
