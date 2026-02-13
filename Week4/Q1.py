# ============================================================
# Question 1: Robot Return to Origin (LeetCode #657)
# Concepts: for loop, if/elif, state tracking, functions
# ============================================================
print("\n" + "=" * 50)
print("Question 1: Robot Return to Origin")
print("=" * 50)


def robot_returns_to_origin(moves):
    """
    Check if robot returns to origin (0,0) after all moves.

    Parameters:
        moves (str): String of moves (U, D, L, R)

    Returns:
        bool: True if robot returns to origin, False otherwise
    """
    # Initialize starting position
    x = 0
    y = 0

    # Loop through each move and update position
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "R":
            x += 1
        elif move == "L":
            x -= 1

    # Return True if back at origin (both x and y are 0)
    return x == 0 and y == 0


# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))



# ============================================================
# BONUS: Alternative Solutions
# ============================================================
print("\n" + "=" * 60)
print("BONUS: ALTERNATIVE SOLUTIONS")
print("=" * 60)

# Alternative Q1: Using count method
print("\n--- Q1 Alternative: Using count() ---")


def robot_returns_to_origin_v2(moves):
    """Alternative: Count U/D and L/R pairs."""
    # Robot returns if equal ups/downs AND equal lefts/rights
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


print("Testing 'UDLR' with count method: " + str(robot_returns_to_origin_v2("UDLR")))
print("Testing 'LLRR' with count method: " + str(robot_returns_to_origin_v2("LLRR")))


# Alternative Q3: Using zip
print("\n--- Q3 Alternative: Using zip() ---")


def shuffle_array_v2(nums, n):
    """Alternative: Use zip to pair elements."""
    first_half = nums[:n]
    second_half = nums[n:]
    result = []

    # zip pairs up elements from both halves
    for x, y in zip(first_half, second_half):
        result.append(x)
        result.append(y)

    return result


print("Shuffle [2,5,1,3,4,7] with zip: " + str(shuffle_array_v2([2, 5, 1, 3, 4, 7], 3)))


# Alternative Q4: Using get() method
print("\n--- Q4 Alternative: Using dict.get() ---")


def count_characters_v2(s):
    """Alternative: Use get() to simplify counting."""
    counts = {}
    for char in s:
        # get() returns 0 if key doesn't exist, then we add 1
        counts[char] = counts.get(char, 0) + 1
    return counts


print("Count 'hello' with get(): " + str(count_characters_v2("hello")))
