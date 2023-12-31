def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    lowerCasedWord = word.lower();
    lowerCasedLetter = letter.lower();

    return lowerCasedWord.count(lowerCasedLetter) if lowerCasedWord.count(lowerCasedLetter) > 0 else 0