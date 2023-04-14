def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.replace(phrase[0], phrase[0].upper())
    space = False
    for i in range(1,len(phrase)):
        if space == True:
            phrase = phrase.replace(phrase[i], phrase[i].upper())
            space = False
        else:
            phrase = phrase.replace(phrase[i], phrase[i].lower())
        if phrase[i] == " ":
            space =True

    return phrase
