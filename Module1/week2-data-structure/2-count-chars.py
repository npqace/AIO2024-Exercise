def count_chars(word):
    """
    This function counts the frequency of each character in a given word.
    Args:
        word: The word to analyze (assumed to be a string).
    Returns:
        A dictionary where each key is a character from the word and the corresponding
        value is the number of times that character appears in the word.
    """

    char_counts = {}  # Initialize an empty dictionary to store character counts
    for char in word:
        """
        Iterate through each character in the word.
        """
        if char in char_counts:
            """
            If the character has already been encountered, increment its count.
            """
            char_counts[char] += 1
        else:
            """
            If the character is new, initialize its count to 1.
            """
            char_counts[char] = 1
    return char_counts

if __name__ == '__main__':
    word = 'Happiness'
    print(count_chars(word))