def levenshtein_distance(source, target):
    """
    Calculates the Levenshtein distance between two strings.

    Args:
        source: The first string.
        target: The second string.

    Returns:
        The Levenshtein distance between the two strings.
    """

    # Get the lengths of the strings and add 1 for base cases
    m = len(source) + 1  # Length of source string + 1
    n = len(target) + 1  # Length of target string + 1

    # Create a matrix to store the Levenshtein distances for prefixes of the strings
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Initialize the first row (base cases for deletion distances)
    for i in range(m):
        dp[i][0] = i  # Deletion cost to transform an empty string to source[0:i]

    # Initialize the first column (base cases for insertion distances)
    for j in range(n):
        dp[0][j] = j  # Insertion cost to transform an empty string to target[0:j]

    # Fill the rest of the matrix using dynamic programming
    for i in range(1, m):  # Start from the second row (i=1)
        for j in range(1, n):  # Start from the second column (j=1)
            if source[i - 1] == target[j - 1]:
                cost = 0  # No cost if characters are the same
            else:
                cost = 1  # Cost of 1 for substitution

            # Calculate the minimum cost for transforming prefixes
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion cost
                dp[i][j - 1] + 1,  # Insertion cost
                dp[i - 1][j - 1] + cost  # Substitution cost
            )

    # Return the Levenshtein distance (bottom right corner of the matrix)
    return dp[m - 1][n - 1]

if __name__ == "__main__":
    source = "kitten"
    target = "sitting"
    print(levenshtein_distance(source, target))
