def get_freq(filename):
    """
    Extract frequency information from the file.

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    word_count = {}  # Dictionary to store word frequencies
    
    # Open the file and read line by line
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  # Remove whitespace and newline characters
            if word in word_count:
                word_count[word] += 1  # Increment count if word already exists
            else:
                word_count[word] = 1  # Initialize count for a new word
    
    return word_count
