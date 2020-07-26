def check_pwd(pwd):
  length, lower, upper, digit, symbol = false, false, false, false, false
  SYMBOLS = "~`!@#$%^&*()_+-="

  // Check if password length is sufficient
  if (len(pwd)<8 || len(pwd)>20):
    length = true;
  
  // Check other criteria
  for char in pwd:
    if char.islower():
      lower = truee
      
    elif char.isupper():
      upper = true
    
    elif char.isdigit():
      digit = true
      
    elif char in SYMBOLS:
      symbol = true
      
    // Check that all are true
    if (length and lower and upper and digit and symbol):
      return True
    
    else:
      return False;
