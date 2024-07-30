import pytest

from src.wordsearch_generator.main import GridGenerator


def test_generate_grid():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3

    # When
    grid = generator.generate_grid(width, length)

    # Then
    assert isinstance(grid, list)
    assert len(grid) == length
    assert all(isinstance(row, list) and len(row) == width for row in grid)

def test_insert_word_in_grid():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3
    word = "hello"

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid(word, grid)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[0][i] == char

    # Check if the rest of the grid cells are empty
    for row in grid:
        for cell in row[len(word):]:
            assert cell == ''