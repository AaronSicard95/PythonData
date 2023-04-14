def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowelCheck = ['a','e','i','o','u']
    vowels = {}
    for i in phrase:
        if i.lower() in vowelCheck:
            if not i.lower() in vowels:
                vowels[i.lower()] = phrase.count(i.lower())+phrase.count(i.upper())
    return vowels
