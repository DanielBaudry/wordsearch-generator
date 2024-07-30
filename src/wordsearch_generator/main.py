from typing import List

class WordDoesNotFitException(Exception):
    pass

class GridGenerator:
    def generate_grid(self, width: int, length: int) -> List[List[str]]:
        return [['' for _ in range(width)] for _ in range(length)]

    def insert_word_in_grid(self, word: str, grid: List[List[str]]) -> None:
        if len(word) > len(grid[0]):
            raise WordDoesNotFitException("Word does not fit in the grid")
        else:
            for i, char in enumerate(word):
                grid[0][i] = char
            for row in grid:
                for i in range(len(word), len(row)):
                    row[i] = ''

    def insert_word_in_grid_vertically(self, word: str, grid: List[List[str]]) -> None:
        if len(word) > len(grid):
            raise WordDoesNotFitException("Word does not fit in the grid")
        else:
            for i, char in enumerate(word):
                grid[i][0] = char
            for col in range(1, len(grid[0])):
                for row in grid:
                    row[col] = ''