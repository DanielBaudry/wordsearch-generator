class GridGenerator:
    def generate_grid(self, width, length):
        return [[''] * width for _ in range(length)]