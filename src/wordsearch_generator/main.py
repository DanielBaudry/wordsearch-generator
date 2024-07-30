from typing import List, Tuple

class WordDoesNotFitException(Exception):
    pass

class GridGenerator:
    def generate_grid(self, width: int, length: int) -> List[List[str]]:
        return [['' for _ in range(width)] for _ in range(length)]

    def insert_word_in_grid_horizontally(self, word: str, grid: List[List[str]]) -> None:
        self.insert_word_in_grid(word, grid, (0, 0))

    def insert_word_in_grid_vertically(self, word: str, grid: List[List[str]]) -> None:
        self.insert_word_in_grid(word, grid, (0, 0), vertical=True)

    def insert_word_in_grid_diagonally(self, word: str, grid: List[List[str]]) -> None:
        self.insert_word_in_grid(word, grid, (0, 0), diagonal=True)

    def insert_word_in_grid(self, word: str, grid: List[List[str]], start_coords: Tuple[int, int], vertical=False, diagonal=False) -> None:
        start_row, start_col = start_coords
        if vertical:
            grid_length = len(grid)
        elif diagonal:
            grid_length = min(len(grid), len(grid[0]))
        else:
            grid_length = len(grid[0])

        if len(word) > grid_length:
            raise WordDoesNotFitException("Word does not fit in the grid")

        for i, char in enumerate(word):
            grid[start_row + i][start_col + i] = char

        for i in range(len(word)):
            for j in range(len(word), len(grid[0])):
                grid[start_row + i][start_col + j] = ''
            for j in range(len(word), len(grid)):
                grid[start_row + j][start_col + i] = ''