from enum import Enum
import random


class WordDirection(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    DIAGONAL = "DIAGONAL"

class Grid:
    words: list[str]
    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.words = []
        self.grid = [["" for _ in range(width)] for _ in range(height)]

    def is_empty_cell(self, row: int, col: int) -> bool:
        return self.grid[row][col] == ""

class WordPlacer:
    def __init__(self, grid: Grid):
        self.grid = grid

    def place_words_in_grid(self, words: list[str]) -> bool:
        for word in words:
            word_is_placed = False
            counter = 0
            while not word_is_placed:
                word_is_placed = self.place_word_in_grid(word)
                if counter > 10000:
                    raise Exception('Word placement failed for word: {word}')
        return True

    def place_word_in_grid(self, word: str) -> bool:
        direction = self.get_random_direction()
        start_row, start_col = self.get_random_empty_cell()
        print(f"Placing word '{word}' in direction {direction}")

        if direction == WordDirection.HORIZONTAL:
            if self.can_place_word_horizontally(start_row, start_col, word):
                self.place_word_horizontally(start_row, start_col, word)
                return True
            return False
        elif direction == WordDirection.VERTICAL:
            if self.can_place_word_vertically(start_row, start_col, word):
                self.place_word_vertically(start_row, start_col, word)
                return True
            return False
        elif direction == WordDirection.DIAGONAL:
            if self.can_place_word_diagonally(start_row, start_col, word):
                self.place_word_diagonally(start_row, start_col, word)
                return True
            return False
    
    def get_random_direction(self) -> WordDirection:
        return random.choice([WordDirection.HORIZONTAL, WordDirection.VERTICAL, WordDirection.DIAGONAL])
        
    def get_random_empty_cell(self) -> tuple[int, int]:
        while True:
            row = random.randint(0, self.grid.height - 1)
            col = random.randint(0, self.grid.width - 1)
            if self.grid.is_empty_cell(row, col):
                return row, col

    def can_place_word_horizontally(self, row: int, col: int, word: str) -> bool:
        if col + len(word) > self.grid.width:
            return False

        for index, letter in enumerate(word):
            if self.grid.grid[row][col + index]!= "" and self.grid.grid[row][col + index]!= letter:
                return False
        return True
    
    def can_place_word_vertically(self, row: int, col: int, word: str) -> bool:
        if row + len(word) > self.grid.height:
            return False
        
        for index, letter in enumerate(word):
            if self.grid.grid[row + index][col]!= "" and self.grid.grid[row + index][col]!= letter:
                return False
            
        return True
    
    def can_place_word_diagonally(self, row: int, col: int, word: str) -> bool:
        if col + len(word) > self.grid.width or row + len(word) > self.grid.height:
            return False
        
        for index, letter in enumerate(word):
            if self.grid.grid[row + index][col + index]!= "" and self.grid.grid[row + index][col + index]!= letter:
                return False
            
        return True
    
    def place_word_horizontally(self, row: int, col: int, word: str):
        for i in range(len(word)):
            self.grid.grid[row][col + i] = word[i]
        self.grid.words.append(word)

    def place_word_vertically(self, row: int, col: int, word: str):
        for i in range(len(word)):
            self.grid.grid[row + i][col] = word[i]
        self.grid.words.append(word)

    def place_word_diagonally(self, row: int, col: int, word: str):
        for i in range(len(word)):
            self.grid.grid[row + i][col + i] = word[i]
        self.grid.words.append(word)

class WordSearchGenerator:
    def generate_word_search(self, width: int, height: int, words: list[str]) -> Grid:
        grid = Grid(width, height)
        placer = WordPlacer(grid)
        placer.place_words_in_grid(words)
        grid = self.fill_grid_with_random_letters(grid)
        return grid

    def fill_grid_with_random_letters(self, grid: Grid) -> Grid:
        random_letters = ""
        for row in range(grid.height):
            for col in range(grid.width):
                if grid.grid[row][col] == "":
                    random_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    grid.grid[row][col] = random_letter
                    random_letters += random_letter
        print(f"Random letters generated: {random_letters} \n")
        return grid

# Example usage

word_search_generator = WordSearchGenerator()
words = ["APPLE", "BANANA", "ORANGE", "GRAPE", "LEMON", "STRAWBERRY", "BLUEBERRY", "CHERRY"]
grid = word_search_generator.generate_word_search(10, 10, words)
for row in grid.grid:
    print("".join(f"[{row or ' '}]"))

print(grid.words)
