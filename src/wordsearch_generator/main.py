class GridGenerator:
    def generate_grid(self, width, length):
        return [[''] * width for _ in range(length)]

    def insert_word_in_grid(self, word, grid):
        # Insert the word in the first row of the grid
        for i, char in enumerate(word):
            grid[0][i] = char