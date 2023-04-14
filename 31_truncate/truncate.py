def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    newPhrase = ""
    if len(phrase)<n:
        return phrase
    elif n <3:
        return "n must be greater than 3"
    else:
        for i in range(0,n-3):
            newPhrase = f"{newPhrase}{phrase[i]}"
        newPhrase = f"{newPhrase}..."
        return newPhrase
