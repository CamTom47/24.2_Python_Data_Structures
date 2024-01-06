def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_list = [];
    case_insensitive_swap = to_swap.swapcase();
    swap_phrase = '';

    for char in phrase:

        if(char == to_swap or char == case_insensitive_swap):
            swap_list.append(char.swapcase());
        
        else:
             swap_list.append(char);

    for char in swap_list:
        swap_phrase += char;
    
    return swap_phrase;
