import random
import pytest

from wordsearch_generator.main import GridGenerator, WordDoesNotFitException

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

def test_insert_word_in_grid_raises_exception():
    # Given
    generator = GridGenerator()
    width = 3
    length = 3
    word = "hello"
    start_coords = (0, 0) 

    # When
    grid = generator.generate_grid(width, length)

    # Then
    with pytest.raises(WordDoesNotFitException):
        generator.insert_word_in_grid_horizontally(word, grid, start_coords)

def test_insert_word_in_grid_horizontally():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3
    word = "hello"
    start_coords = (0, 0)  # Updated starting coordinates

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_horizontally(word, grid, start_coords)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[start_coords[0]][start_coords[1] + i] == char

    # Check if the rest of the grid cells are empty
    for row in grid:
        for cell in row[:start_coords[1]] + row[start_coords[1] + len(word):]:
            assert cell == ''

def test_insert_word_in_grid_vertically():
    # Given
    generator = GridGenerator()
    width = 3
    length = 5
    word = "hello"
    start_coords = (0, 0)  # Updated starting coordinates

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_vertically(word, grid, start_coords)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[start_coords[0] + i][start_coords[1]] == char

    # Check if the rest of the grid cells are empty
    for col in range(start_coords[1]):
        for row in grid:
            assert row[col] == ''
    for col in range(start_coords[1] + len(word), width):
        for row in grid:
            assert row[col] == ''

def test_insert_word_in_grid_diagonally():
    # Given
    generator = GridGenerator()
    width = 5
    length = 5
    word = "hello"
    start_coords = (0, 0)  # Updated starting coordinates

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_diagonally(word, grid, start_coords)

    # Then
    # Check if the word is inserted correctly in the grid
    for i, char in enumerate(word):
        assert grid[start_coords[0] + i][start_coords[1] + i] == char

    # Check if the rest of the grid cells are empty
    for i in range(start_coords[0]):
        for j in range(start_coords[1]):
            assert grid[i][j] == ''
    for i in range(start_coords[0] + len(word), length):
        for j in range(start_coords[1] + len(word), width):
            assert grid[i][j] == ''

def test_insert_word_in_grid_raises_overlap_exception():
    # Given
    generator = GridGenerator()
    width = 5
    length = 3
    existing_word = "hello"
    new_word = "hlelo"  # New word with overlapping letters
    start_coords = (0, 0)  # Updated starting coordinates

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_horizontally(existing_word, grid, start_coords)

    # Then
    with pytest.raises(WordDoesNotFitException):
        generator.insert_word_in_grid_horizontally(new_word, grid, start_coords)

def test_insert_word_in_grid_overlap_same_letter():
    # Given
    generator = GridGenerator()
    width = 5
    length = 5
    word1 = "hello"
    word2 = "world"

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_horizontally(word1, grid, start_coords=(1, 0))
    generator.insert_word_in_grid_vertically(word2, grid, start_coords=(0, 4))

    # Then
    generator.print_grid(grid)
    assert True

def test_insert_word_in_grid_different_lengths_and_orientations():
    # Given
    generator = GridGenerator()
    width = 10
    length = 10
    words = ["hello", "world", "python", "java", "testing"]
    orientations = ["horizontal", "vertical", "diagonal"]

    # When
    grid = generator.generate_grid(width, length)
    for word, orientation in zip(words, orientations):
        if orientation == "horizontal":
            start_coords = (random.randint(0, length - 1), random.randint(0, width - len(word)))
            generator.insert_word_in_grid_horizontally(word, grid, start_coords)
        elif orientation == "vertical":
            start_coords = (random.randint(0, length - len(word)), random.randint(0, width - 1))
            generator.insert_word_in_grid_vertically(word, grid, start_coords)
        elif orientation == "diagonal":
            start_coords = (random.randint(0, length - len(word)), random.randint(0, width - len(word)))
            generator.insert_word_in_grid_diagonally(word, grid, start_coords)

    # Then
    generator.print_grid(grid)
    # Check if all words are inserted correctly in the grid
    for word, orientation in zip(words, orientations):
        if orientation == "horizontal":
            for i, char in enumerate(word):
                assert grid[start_coords[0]][start_coords[1] + i] == char
        elif orientation == "vertical":
            for i, char in enumerate(word):
                assert grid[start_coords[0] + i][start_coords[1]] == char
        elif orientation == "diagonal":
            for i, char in enumerate(word):
                assert grid[start_coords[0] + i][start_coords[1] + i] == char