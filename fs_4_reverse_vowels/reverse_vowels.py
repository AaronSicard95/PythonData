def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    newPhrase = ""
    vowelCheck = ['a','e','i','o','u','A','E','I','O','U']
    vowels = []
    for i in s:
        if i in vowelCheck:
            vowels.append(i)
    vowels.reverse()
    print(vowels)
    pos = 0
    for i in s:
        if i in vowelCheck:
            print(vowels[pos])
            newPhrase = f"{newPhrase}{vowels[pos]}"
            pos = pos+1
        else:
            newPhrase = f"{newPhrase}{i}"
    return newPhrase