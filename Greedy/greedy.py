class GreedySquaresCalculator:
    @staticmethod
    def calculate_minimum_squares(length, width):
        squares = []  # List to store sizes of squares
        square_counts = {}  # Dictionary to store count of each square size

        # Swap length and width if length is smaller than width
        length, width = max(length, width), min(length, width)

        while length > 0 and width > 0:
            square_size = min(length, width)
            squares.append(square_size)
            square_counts[square_size] = square_counts.get(square_size, 0) + 1
            if length > width:
                length -= square_size
            else:
                width -= square_size

        total_squares = sum(square_counts.values())
        return square_counts, total_squares


class DynamicSquaresCalculator:
    @staticmethod
    def calculate_minimum_squares(length, width):
        dp = [[float("inf")] * (width + 1) for _ in range(length + 1)]

        # Calculate the minimum number of squares for each subproblem
        for i in range(1, length + 1):
            for j in range(1, width + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    for k in range(1, i // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j])
                    for k in range(1, j // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k])

        total_squares = dp[length][width]

        squares = []
        while length > 0 and width > 0:
            square_size = min(length, width)
            squares.append(square_size)
            if length > width:
                length -= square_size
            else:
                width -= square_size

        # Count the occurrence of each square size
        square_counts = {square: squares.count(square) for square in set(squares)}

        return square_counts, total_squares


# Define colors for output statements
LAND_COLOR = "\033[1;36m"  # Bright cyan
SQUARE_COLOR = "\033[1;35m"  # Bright purple
COUNT_COLOR = "\033[1;33m"  # Bright yellow
HEADER_COLOR = "\033[1;32m"  # Bright green
TOTAL_COLOR = "\033[1;31m"  # Bright red
RESET_COLOR = "\033[0m"  # Reset to default color
SEPARATOR_COLOR = "\033[1;34m"  # Bright blue


def get_land_dimensions():
    # Get the dimensions of the land from the user
    length = int(input(f"Enter the {LAND_COLOR}length{RESET_COLOR} of the land: "))
    width = int(input(f"Enter the {LAND_COLOR}width{RESET_COLOR} of the land: "))
    return length, width


def print_square_counts(title, square_counts, total):
    # Print the squares with their sizes and counts
    print(f"\n{HEADER_COLOR}{title}: Squares with their sizes and counts:{RESET_COLOR}")
    for square, count in square_counts.items():
        print(
            f"{COUNT_COLOR}{count}{RESET_COLOR} x ({SQUARE_COLOR}{square} x {square}{RESET_COLOR}) km²"
        )
    # Print the total number of squares
    print(
        f"{HEADER_COLOR}{title}: Total number of squares:{RESET_COLOR} {TOTAL_COLOR}{total}{RESET_COLOR}"
    )


def print_separator():
    # Print a separator line with color
    separator = f"{RESET_COLOR}\n{SEPARATOR_COLOR}{'=' * 40}{RESET_COLOR}\n"
    print(separator)


# Main program
length, width = get_land_dimensions()

# Calculate the counts and total number of squares using the greedy algorithm
greedy_calculator = GreedySquaresCalculator()
greedy_square_counts, greedy_total = greedy_calculator.calculate_minimum_squares(
    length, width
)

# Calculate the counts and total number of squares using the dynamic programming algorithm
dynamic_calculator = DynamicSquaresCalculator()
dynamic_square_counts, dynamic_total = dynamic_calculator.calculate_minimum_squares(
    length, width
)

# Print the squares and counts using the greedy algorithm
print_square_counts("Greedy", greedy_square_counts, greedy_total)
print_separator()
# Print the squares and counts using the dynamic programming algorithm
print_square_counts("Dynamic", dynamic_square_counts, dynamic_total)
