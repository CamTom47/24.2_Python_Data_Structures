def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    reversedPhrase = '';
    phraseList = [];

    for char in phrase:
        phraseList.append(char);

    phraseList.reverse();

    for char in phraseList:
        reversedPhrase += char;

    return reversedPhrase;