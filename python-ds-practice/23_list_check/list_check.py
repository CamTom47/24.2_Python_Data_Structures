def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    false_list = [];
    
    for item in lst:
        if(isinstance(item , list) != True):
            false_list.append(item);

    if(len(false_list) != 0):
        return False;

    else:
        return True;
