# CS362-SU20, A2-TDD
# Ryan Stachura
# Oregon State University

SYMBOLS = "~`!@#$%^&*()_+-="

def check_pwd(pwd):

    if any(char.islower() for char in pwd):
        return True

    return False
