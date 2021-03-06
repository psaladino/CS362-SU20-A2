# CS362-SU20, A2-TDD
# Ryan Stachura
# Oregon State University

SYMBOLS = "~`!@#$%^&*()_+-="

def check_pwd(pwd):

    if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd) and any(char.isdigit() for char in pwd) and any(char in SYMBOLS for char in pwd) and len(pwd)>=8 and len(pwd)<=20:
        return True

    return False
