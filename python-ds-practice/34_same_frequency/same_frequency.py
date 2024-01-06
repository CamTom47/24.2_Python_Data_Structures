def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1);
    num2 = str(num2);
    
    dict1 = {};
    for num in num1:
        dict1[num] = dict1.get(num, 0) + 1;

    dict2 = {};
    for num in num2:
        dict2[num] = dict2.get(num, 0) + 1;

    if(dict1 == dict2):
        return True;
    
    else:
        return False;