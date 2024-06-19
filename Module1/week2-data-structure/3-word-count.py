def word_count(file_path):
    """
    This function counts the frequency of words in a text file.

    Args:
        file_path: The path to the text file to analyze (assumed to be a string).

    Returns:
        A dictionary where each key is a word from the file (in lowercase) and the
        corresponding value is the number of times that word appears in the file.
    """

    result = {}  # Initialize an empty dictionary to store word counts

    # Open the file in read mode with context manager
    with open(file_path, 'r') as f:
        for line in f:
            """
            Iterate through each line in the file.
            """
            words = line.split()  # Split the line into individual words

            for word in words:
                """
                Iterate through each word in the current line.
                """
                word = word.lower()  # Convert the word to lowercase for case-insensitive counting

                if word in result:
                    """
                    Check if the word has already been encountered.
                    """
                    result[word] += 1  # Increment its count if found
                else:
                    """
                    If the word is new, initialize its count to 1.
                    """
                    result[word] = 1

    return result

if __name__ == '__main__':
    file_path = 'P1_data.txt'
    print(word_count(file_path))