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
    length = 3
    word1 = "hello"
    word2 = "wolrd"  # Updated word
    start_coords = (0, 0)  # Updated starting coordinates

    # When
    grid = generator.generate_grid(width, length)
    generator.insert_word_in_grid_horizontally(word1, grid, start_coords)
    generator.insert_word_in_grid_vertically(word2, grid, start_coords=(0, 2))  # Updated starting coordinates

    # Then
    # Check if the second word overlaps with the first word at the same letter
    assert grid[0][2] == 'l'  # Overlapping letter 'l'
    assert grid[1][2] == 'l'  # Overlapping letter 'l'

    # Check if the rest of the grid cells are empty
    for row in grid:
        for cell in row[3:]:
            assert cell == ''

    generator.print_grid(grid)