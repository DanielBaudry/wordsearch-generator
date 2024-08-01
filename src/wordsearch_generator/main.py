from pprint import pprint
from typing import List, Tuple

class WordDoesNotFitException(Exception):
    pass

class GridGenerator:
    def generate_grid(self, width: int, length: int) -> List[List[str]]:
        return [['' for _ in range(width)] for _ in range(length)]

    def insert_word_in_grid_horizontally(self, word: str, grid: List[List[str]], start_coords: Tuple[int, int]) -> None:
        self.insert_word_in_grid(word, grid, start_coords)

    def insert_word_in_grid_vertically(self, word: str, grid: List[List[str]], start_coords: Tuple[int, int]) -> None:
        self.insert_word_in_grid(word, grid, start_coords, vertical=True)

    def insert_word_in_grid_diagonally(self, word: str, grid: List[List[str]], start_coords: Tuple[int, int]) -> None:
        self.insert_word_in_grid(word, grid, start_coords, diagonal=True)
    
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
            if vertical:
                if grid[start_row + i][start_col] != '' and grid[start_row + i][start_col] != char:
                    raise WordDoesNotFitException("Word overlaps with existing letters in the grid")
                grid[start_row + i][start_col] = char
            elif diagonal:
                if grid[start_row + i][start_col + i] != '' and grid[start_row + i][start_col + i] != char:
                    raise WordDoesNotFitException("Word overlaps with existing letters in the grid")
                grid[start_row + i][start_col + i] = char
            else:
                if grid[start_row][start_col + i] != '' and grid[start_row][start_col + i] != char:
                    raise WordDoesNotFitException("Word overlaps with existing letters in the grid")
                grid[start_row][start_col + i] = char    

    def print_grid(self, grid: List[List[str]]) -> None:
        pprint(grid)