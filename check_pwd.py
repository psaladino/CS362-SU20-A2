def check_pwd(pwd):
    """length, lower, upper, digit, symbol = False, False, False, False, False
    SYMBOLS = "~`!@#$%^&*()_+-="

    # Check if password length is sufficient
    if (len(pwd)>=8 and len(pwd)<=20):
        length = True;
  
    # Check other criteria
    for char in pwd:
        if char.islower():
            lower = True
      
        elif char.isupper():
            upper = True
    
        elif char.isdigit():
            digit = True
      
        elif char in SYMBOLS:
            symbol = True
      
    # Check that all are true
    if (length and lower and upper and digit and symbol):
        return True
    
    else:
        return False"""
    
    return True
