def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    lstLen = len(lst);

    return lst[lstLen-1] if (lstLen > 0) else None;    